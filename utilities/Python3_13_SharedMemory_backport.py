"""Mimick the 3.13 version of `multiprocessing.SharedMemory` with the
`track` argument. This is done by temporarily disabling
`multiprocessing.SharedMemory` registrations to the resource tracker
during instantiation, as well as slightly modifying the
`multiprocessing.SharedMemory.unlink` method in the subclass to only
attempt the unregistration process if we have enabled tracking.

"""

import sys
import threading
from typing import Union
from multiprocessing import resource_tracker as _mprt
from multiprocessing import shared_memory as _mpshm


if sys.version_info >= (3, 13):
    SharedMemory = _mpshm.SharedMemory
else:
    class SharedMemory(_mpshm.SharedMemory):
        __lock = threading.Lock()

        def __init__(
            self, name: Union[None, str] = None, create: bool = False,
            size: int = 0, *, track: bool = True
        ) -> None:
            self._track = track

            # if tracking, normal init will suffice
            if track:
                return super().__init__(name=name, create=create, size=size)

            # lock so that other threads don't attempt to use the
            # register function during this time
            with self.__lock:
                # create a temporary registration function
                def tmp_register(*args, **kwargs) -> None:
                    return

                # temporarily disable registration during initialization
                try:
                    orig_register = _mprt.register
                    _mprt.register = tmp_register

                    # initialize
                    super().__init__(name=name, create=create, size=size)
                finally:
                    # ensure original register function is re-instated
                    _mprt.register = orig_register

        def unlink(self) -> None:
            if _mpshm._USE_POSIX and self._name:
                _mpshm._posixshmem.shm_unlink(self._name)
                if self._track:
                    _mprt.unregister(self._name, "shared_memory")
