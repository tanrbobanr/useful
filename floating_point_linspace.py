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


class linspace(Sequence[float]):
    """Generates linearly spaced values in a given range. Values are
    generated dynamically (on an as-needed basis).

    """
    __SupportsDecimalConversion: TypeAlias = Union[
        decimal.Decimal, numbers.Real, numbers.Integral
    ]

    def __init__(
        self, start: __SupportsDecimalConversion,
        stop: __SupportsDecimalConversion, count: numbers.Integral
    ):
        if not isinstance(count, numbers.Integral) or count <= 1:
            raise ValueError('count must be an integer > 1')

        self._start = self._to_dec(start)
        self._stop = self._to_dec(stop)
        self._count = self._to_dec(count)
        self._step: decimal.Decimal = (self._stop - self._start) / (count - 1)

    @staticmethod
    def _to_dec(value: __SupportsDecimalConversion) -> decimal.Decimal:
        return (
            value if isinstance(value, decimal.Decimal)
            else decimal.Decimal(str(value))
        )

    @property
    def start(self) -> float:
        return float(self._start)

    @property
    def stop(self) -> float:
        return float(self._stop)

    @property
    def count(self) -> int:
        return self._count

    @property
    def step(self) -> float:
        return float(self._step)

    def __len__(self) -> int:
        return self._count

    @overload
    def __getitem__(self, index: int, /) -> float: ...
    @overload
    def __getitem__(self, index: slice, /) -> Tuple[float, ...]: ...
    def __getitem__(
        self, index: Union[int, slice], /
    ) -> Union[float, Tuple[float, ...]]:
        if isinstance(index, slice):
            return tuple(self[x] for x in range(*index.indices(self._count)))
        if index < 0:
            index += self._count
        if index >= self._count:
            raise IndexError("linspace object index out of range")
        if index == self._count - 1:
            return float(self._stop)
        return float(self._start + (self._step * index))

    def __repr__(self) -> str:
        return "{}({}, {}, {})".format(
            type(self).__name__,
            self._start,
            self._stop,
            self._count
        )

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, type(self)):
            return False

        return (
            (self._start, self._stop, self._count)
            == (other.start, other.stop, other.count)
        )

    def __ne__(self, other: Any) -> bool:
        return not (self == other)

    def __hash__(self) -> int:
        return hash((type(self), self._start, self._stop, self._count))
