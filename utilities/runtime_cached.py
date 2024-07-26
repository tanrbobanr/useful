import sys
from typing import TypeVar
if sys.version_info >= (3, 10):
    from typing import ParamSpec
else:
    from typing_extensions import ParamSpec
if sys.version_info >= (3, 9):
    from collections.abc import Callable
else:
    from typing import Callable


_T = TypeVar("_T")
_P = ParamSpec("_P")


def runtime_cached(
    *args: _P.args, **kwargs: _P.kwargs
) -> Callable[[Callable[_P, _T], _T], _T]:
    """Runs the decorated function and caches its value at runtime. This
    is essentially a more readible and typing-correct version of the
    `@lambda _: _()` decorator. If desired, positional and/or keyword
    arguments may be passed in, which will be used when calling the
    decorated function.

    """
    def inner(fn: Callable[_P, _T]) -> _T:
        return fn(*args, **kwargs)
    return inner
