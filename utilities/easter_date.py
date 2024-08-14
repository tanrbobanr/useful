def easter_date(year: int) -> datetime.date:
    """Calculate the date of Easter for a given year after. This uses
    Jean Meeus' algorithm which was first published in Astronomical
    Algorithms, and was later described in Donald Knuth's Art of
    Computer Programming, Volume I, Fundamental Algorithms
    (Procedure 38.4. Algorithm B).

    This function has a time complexity of O(1) and a space complexity
    of O(1).

    """
    a = year % 19
    b, c = divmod(year, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    q = (h + l - 7 * m + 114)
    n = q // 31
    p = q % 31
    return datetime.date(
        year=year,
        month=n,
        day=(p + 1)
    )
