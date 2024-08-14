def nth_dow(
    year: int, month: int, dow: int, n: int
) -> datetime.date:
    """Get the Nth day of week for a given year and month. `n` starts
    at `1`.

    """
    d = datetime.date(year, month, 1)
    return d.replace(day=(dow - d.weekday()) % 7 + (n - 1) * 7 + 1)
