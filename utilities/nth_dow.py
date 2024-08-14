def nth_dow(
    year: int, month: int, dow: int, n: int, day: int = 1
) -> datetime.date:
    """Get the Nth day of week for a given year and month. `n` starts
    at `1`. If `day` is given, it will be used for the starting date (
    e.g. if `day` lands on a Sunday, and `n=1`, the next Sunday will be
    selected).

    """
    d = datetime.date(year, month, day)
    return d.replace(day=(dow - d.weekday()) % 7 + (n - 1) * 7 + 1)
