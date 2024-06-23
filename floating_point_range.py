"""A class similar to `range`, but allows for the use of floating point
numbers. Uses the `decimal` standard library to ensure accuracy.

"""


import sys
import numbers
import decimal
from typing import (
    Tuple,
    Union,
    overload,
)
if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


class frange(Sequence[float]):
    @overload
    def __init__(
        self, stop: Union[decimal.Decimal, numbers.Real], /
    ) -> None: ...
    @overload
    def __init__(
        self, start: Union[decimal.Decimal, numbers.Real],
        stop: Union[decimal.Decimal, numbers.Real],
        step: Union[decimal.Decimal, numbers.Real] = ..., /
    ) -> None: ...
    def __init__(self, *args: Union[decimal.Decimal, numbers.Real]) -> None:
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
    def __to_dec(
        value: Union[numbers.Real, numbers.Integral, decimal.Decimal]
    ) -> decimal.Decimal:
        return (
            value if isinstance(value, decimal.Decimal)
            else decimal.Decimal(str(value))
        )

    @classmethod
    def __parse_args(
        cls, args: Tuple[Union[decimal.Decimal, numbers.Real], ...]
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

    def __hash__(self):
        return hash((type(self), self.__start, self.__stop, self.__step))

    def count(self, value: Union[decimal.Decimal, numbers.Real], /) -> int:
        dec = self.__to_dec(value)
        if dec % self.__step:
            return 0
        low, high = sorted((
            self.__start,
            self.__start + self.__step * (self.__len - 1)
        ))
        return int(low <= dec < high)

    def index(self, value: Union[decimal.Decimal, numbers.Real], /) -> int:
        dec = self.__to_dec(value)
        index = (dec - self.__start) / self.__step
        if index % 1 or index >= self.__len:
            raise ValueError(f"{value} is not in frange")
        return int(index)
