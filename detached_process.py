"""A version of `multiprocessing.Process` that does not get cleaned up
when the spawning process closes. This is done by immediately removing
itself from the internal `multiprocess.process._children` set (which is
used during cleanup) after being started.

"""

import multiprocessing as _mp
import multiprocessing.process as _mppr


class DetachedProcess(_mp.Process):
    def start(self) -> None:
        super().start()
        _mppr._children.discard(self)
