"""A class similar to `range`, but allows for the use of floating point
numbers. Uses the `decimal` standard library to ensure accuracy.

"""


import sys
import numbers
import decimal
from typing import (
    Any,
    Tuple,
    Union,
    overload,
)

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


class frange(Sequence[float]):
    """Works similarly to `range`, but allows for floating point values
    to be used. See `help(range)` for more information on how to use the
    object.

    """
    __SupportsDecimalConversion: TypeAlias = Union[
        decimal.Decimal, numbers.Real, numbers.Integral
    ]

    @overload
    def __init__(
        self, stop: __SupportsDecimalConversion, /
    ) -> None: ...
    @overload
    def __init__(
        self, start: __SupportsDecimalConversion,
        stop: __SupportsDecimalConversion,
        step: __SupportsDecimalConversion = ..., /
    ) -> None: ...
    def __init__(
        self, *args: __SupportsDecimalConversion
    ) -> None:
        (
            self.__start, self.__stop, self.__step, self.__len
        ) = self.__parse_args(args)

    @property
    def start(self) -> float:
        return float(self.__start)

    @property
    def stop(self) -> float:
        return float(self.__stop)

    @property
    def step(self) -> float:
        return float(self.__step)

    @staticmethod
    def __to_dec(value: __SupportsDecimalConversion) -> decimal.Decimal:
        return (
            value if isinstance(value, decimal.Decimal)
            else decimal.Decimal(str(value))
        )

    @classmethod
    def __parse_args(
        cls, args: Tuple[__SupportsDecimalConversion, ...]
    ) -> Tuple[decimal.Decimal, decimal.Decimal, decimal.Decimal, int]:
        dec_args = tuple(map(cls.__to_dec, args))
        num_args = len(args)
        if num_args == 1:
            (start, stop, step) = (
                decimal.Decimal(0), dec_args[0], decimal.Decimal(1)
            )
        elif num_args == 2:
            (start, stop, step) = (*dec_args, decimal.Decimal(1))
        elif num_args == 3:
            (start, stop, step) = dec_args
        else:
            raise TypeError(
                "frange() takes between 1 and 3 positional arguments"
                f" (inclusive) but {num_args} was given"
            )

        # determine length
        diff = ((start - stop) if step < 0 else (stop - start))
        length = max(0, int(
            diff // abs(step) - (not (diff % step))
        ) + 1)

        return (start, stop, step, length)

    def __len__(self) -> int:
        return self.__len

    @overload
    def __getitem__(self, index: int, /) -> float: ...
    @overload
    def __getitem__(self, index: slice, /) -> Tuple[float, ...]: ...
    def __getitem__(
        self, index: Union[int, slice], /
    ) -> Union[float, Tuple[float, ...]]:
        if isinstance(index, slice):
            return tuple(
                self[x] for x in range(*index.indices(self.__len))
            )
        if index < 0:
            index += self.__len
        if index >= self.__len:
            raise IndexError("frange object index out of range")
        return float(self.__start + self.__step * index)

    def __repr__(self) -> str:
        return "{}({}, {}, {})".format(
            type(self).__name__, self.__start, self.__stop, self.__step
        )

    def __eq__(self, other: Any, /) -> bool:
        if not isinstance(other, type(self)):
            return False
        return (
            (self.__start, self.__stop, self.__step)
            == (other.start, other.stop, other.step)
        )

    def __ne__(self, other: Any, /) -> bool:
        return not (self == other)

    def __hash__(self) -> int:
        return hash((type(self), self.__start, self.__stop, self.__step))

    def count(self, value: __SupportsDecimalConversion, /) -> int:
        """Return the number of occurrences of `value`"""
        dec = self.__to_dec(value)
        if dec % self.__step:
            return 0
        low, high = sorted((
            self.__start,
            self.__start + self.__step * (self.__len - 1)
        ))
        return int(low <= dec < high)

    def index(self, value: __SupportsDecimalConversion, /) -> int:
        """Return the index of `value`. Raise ValueError if the value is not
        present.

        """
        dec = self.__to_dec(value)
        index = (dec - self.__start) / self.__step
        if index % 1 or index >= self.__len:
            raise ValueError(f"{value} is not in frange")
        return int(index)
