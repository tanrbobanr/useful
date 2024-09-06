#! /usr/bin/env python3
import sys
import pathlib
import argparse
import datetime
import itertools
from typing import (
    List,
    TypeVar,
    Union,
)
if sys.version_info >= (3, 9):
    from collections.abc import Callable
else:
    from typing import Callable


_T = TypeVar("_T")
FILE = pathlib.Path(__file__)
FULL_DT_FORMAT = r"%Y-%m-%dT%H:%M:%S"
DT_PARSE_FORMATS = (
    r"%Y-%m-%dT%H:{}", # %M:%S
    r"%Y-%m-%dT{}",    # %H:%M:%S
    r"%Y-%m-{}",       # %dT%H:%M:%S
    r"%Y-{}",          # %m-%dT%H:%M:%S
    None,              # %Y-%m-%dT%H:%M:%S
    r"{}:%S",          # %Y-%m-%dT%H:%M
    r"{}:%M:%S",       # %Y-%m-%dT%H
    r"{}T%H:%M:%S",    # %Y-%m-%d
    r"{}-%dT%H:%M:%S", # %Y-%m
)
DT_PARSE_OPTIONS = (
    r"",
    r"%z",
)
SPY = 31_557_600
SPM = 2_629_800
SPW = 604_800
SPD = 86_400
SPH = 3_600
SPI = 60


def parse_dt(dtstr: str) -> datetime.datetime:
    """Attempt to detect and parse a datetime"""
    now = datetime.datetime.now().astimezone()
    dtstr = dtstr.strip()

    for fmt, opt in itertools.product(
        DT_PARSE_FORMATS, DT_PARSE_OPTIONS
    ):
        try:
            return datetime.datetime.strptime(
                now.strftime(fmt).format(dtstr) if fmt else dtstr,
                FULL_DT_FORMAT + opt
            )
        except ValueError:
            continue

    raise ValueError(f"Invalid datetime: {dtstr!r}")


def parse_ts(tsstr: str) -> datetime.timedelta:
    """Parse a timestamp string formatted as `T[+|-][[[dd:]hh:]mm:]ss`.

    """
    # just T[+|-]
    if len(tsstr) == 2:
        return datetime.timedelta(seconds=0)

    sign = (1, -1)[tsstr[1] == "+"]
    s = 0
    muls = (1, SPI, SPH, SPD)

    for m, p in zip(muls, reversed(tuple(map(int, tsstr[2:].split(":"))))):
        s += p * m
    return datetime.timedelta(seconds=(s * sign))


def parse_dt_or_ts(dt_or_ts: str) -> datetime.datetime:
    """Attempt to parse a datetime or timestamp (offset from current
    time) using one of `parse_dt` or `parse_ts`.

    """
    dt_or_ts = dt_or_ts.upper()

    # timestamp
    if dt_or_ts.startswith("T-") or dt_or_ts.startswith("T+"):
        return datetime.datetime.now(
            datetime.timezone.utc
        ).astimezone() + parse_ts(dt_or_ts)
    
    return parse_dt(dt_or_ts)


class Argspec:
    """Represents one of the time formats supported by Discord's unix
    timestamp system (one of `tTdDfFR`). Contains information on how the
    format should be added to the argument parser, as well as how it
    should be listed and formatted when using the `-l` option in the
    command line.

    """
    name: str
    flag: str
    desc: str
    eg12: str
    eg24: str
    fmt12: Callable[[datetime.datetime], str]
    fmt24: Callable[[datetime.datetime], str]

    @staticmethod
    def strftime(fmt: str) -> Callable[[datetime.datetime], str]:
        def f(dt: datetime.datetime) -> str:
            return dt.strftime(fmt)
        return f


class Argspecs(List[Argspec]):
    """A glorified list to store `_Argspec` instances"""
    def register(self, cls: _T) -> _T:
        self.append(cls)
        return cls


ARGSPECS = Argspecs()


@ARGSPECS.register
class short_time(Argspec):
    name = "short-time"
    flag = "t"
    eg12 = "4:20 PM"
    eg24 = "16:20"
    desc = "short time"
    fmt24 = Argspec.strftime(r"%H:%M")

    @staticmethod
    def fmt12(dt: datetime.datetime) -> str:
        return dt.strftime(r"%I:%M %p")[(0, 1)[((dt.hour - 1) % 12) <= 9]:]


@ARGSPECS.register
class long_time(Argspec):
    name = "long-time"
    flag = "T"
    eg12 = "4:20:30 PM"
    eg24 = "16:20:30"
    desc = "long time"
    fmt24 = Argspec.strftime(r"%H:%M:%S")

    @staticmethod
    def fmt12(dt: datetime.datetime) -> str:
        return dt.strftime(r"%I:%M:%S %p")[(0, 1)[((dt.hour - 1) % 12) <= 9]:]


@ARGSPECS.register
class short_date(Argspec):
    name = "short-date"
    flag = "d"
    eg12 = "04/20/2021"
    eg24 = "20/04/2021"
    desc = "short date"
    fmt12 = Argspec.strftime(r"%m/%d/%Y")
    fmt24 = Argspec.strftime(r"%d/%m/%Y")


@ARGSPECS.register
class long_date(Argspec):
    name = "long-date"
    flag = "D"
    eg12 = "April 20, 2011"
    eg24 = "20 April 2021"
    desc = "long date"

    @staticmethod
    def fmt12(dt: datetime.datetime) -> str:
        return dt.strftime(r"%B {}, %Y").format(dt.day)

    @staticmethod
    def fmt24(dt: datetime.datetime) -> str:
        return dt.strftime(r"{} %B %Y").format(dt.day)


@ARGSPECS.register
class short_datetime(Argspec):
    name = "short-datetime"
    flag = "f"
    eg12 = "April 20, 2021 4:20 PM"
    eg24 = "20 April 2021 16:20"
    desc = "[DEFAULT] short date/time"

    @staticmethod
    def fmt12(dt: datetime.datetime) -> str:
        return dt.strftime(r"%B {}, %Y {}:%M %p").format(
            dt.day,
            (dt.hour % 12) or 12
        )

    @staticmethod
    def fmt24(dt: datetime.datetime) -> str:
        return dt.strftime(r"{} %B %Y %H:%M").format(dt.day)


@ARGSPECS.register
class long_datetime(Argspec):
    name = "long-datetime"
    flag = "F"
    eg12 = "Tuesday, April 20, 2021 4:20 PM"
    eg24 = "Tuesday, 20 April 2021 16:20"
    desc = "long date/time"

    @staticmethod
    def fmt12(dt: datetime.datetime) -> str:
        return dt.strftime(r"%A, %B {}, %Y {}:%M %p").format(
            dt.day,
            (dt.hour % 12) or 12
        )

    @staticmethod
    def fmt24(dt: datetime.datetime) -> str:
        return dt.strftime(r"%A, {} %B %Y %H:%M").format(dt.day)


@ARGSPECS.register
class relative_time(Argspec):
    name = "relative-time"
    flag = "R"
    eg12 = "3 years ago"
    eg24 = "3 years ago"
    desc = "relative time"
    
    @staticmethod
    def fmt12(dt: datetime.datetime) -> str:
        period_names = (
            "year", "month", "week", "day", "hour", "minute", "second"
        )
        divisors = (SPY, SPM, SPW, SPD, SPH, SPI, 1)
        now = datetime.datetime.now().astimezone()

        # get delta and which template to use
        template, delta = (
            ("in {}", dt - now)
            if dt > now
            else ("{} ago", now - dt)
        )

        # format output
        s = int(delta.total_seconds())
        for i, (name, divisor) in enumerate(zip(period_names, divisors)):
            diff = s / divisor
            if diff < 1:
                continue

            value = round(diff)

            # if value is rounded up to the minimum of the previous
            # iteration, use the previous iteration's value instead
            # (e.g. if divisor=SPI and value=60, then we should instead
            # use divisor=SPH and value=1)
            if i and value == divisors[i - 1] // divisor:
                name = period_names[i - 1]
                value = round(s / divisors[i - 1])

            prefix, suffix = (
                (value, "s"),
                (("a", "an")[name == "hour"], "")
            )[value == 1]

            return template.format(f"{prefix} {name}{suffix}")

        # default
        return template.format("a second")

    fmt24 = fmt12


def make_parser() -> argparse.ArgumentParser:
    """Create the argument parser"""
    p = argparse.ArgumentParser(FILE.name)
    p.add_argument(
        type=parse_dt_or_ts,
        dest="datetime",
        metavar="DATETIME"
    )

    # add optional arguments
    g = p.add_mutually_exclusive_group()
    g.add_argument(
        "-l",
        "--list",
        dest="option",
        help=(
            "List available options and how they would be formatted using"
            " the given datetime"
        ),
        action="store_const",
        const="l"
    )
    for spec in ARGSPECS:
        g.add_argument(
            f"-{spec.flag}",
            f"--{spec.name}",
            dest="option",
            help=(
                f"{spec.desc} (e.g. `{spec.eg12}' for 12-hour and"
                f" `{spec.eg24}' for 24-hour)"
            ),
            action="store_const",
            const=spec.flag
        )

    return p


def list_options(dt: datetime.datetime) -> None:
    """List all options and how the given datetime would be represented
    when using them.

    """
    for spec in ARGSPECS:
        print(f"-{spec.flag}, --{spec.name}")
        print(f"    12-hour : {spec.fmt12(dt.astimezone())}")
        print(f"    24-hour : {spec.fmt24(dt.astimezone())}")


def handle_input(dt: datetime.datetime, opt: Union[str, None]) -> None:
    """Handle the user input from the argument parser"""
    if opt == "l":
        return list_options(dt)
    suffix = f":{opt}" if opt else ""
    print(f"<t:{int(dt.timestamp())}{suffix}>")


def main() -> None:
    """Run the argument parser, then handle the input"""
    ps = make_parser()
    ns = ps.parse_args()
    kw = dict(ns._get_kwargs())
    handle_input(kw["datetime"], kw.get("option"))


if __name__ == "__main__":
    main()
