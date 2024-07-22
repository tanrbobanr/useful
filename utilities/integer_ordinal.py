def ordinal_suffix(n: int) -> str:
    """Returns the ordinal suffix of the given integer.

    Example
    -------
    ```
    >>> ordinal_suffix(0)
    'th'
    >>> ordinal_suffix(343)
    'rd'
    ```

    """
    return (
        "th" if (11 <= (n % 100) <= 13)
        else ("th", "st", "nd", "rd", "th")[min(n % 10, 4)]
    )


def to_ordinal(n: int) -> str:
    """Convert an integer into its ordinal representation.

    Example
    -------
    ```
    >>> to_ordinal(0)
    '0th'
    >>> to_ordinal(343)
    '343rd'
    ```

    """
    # don't call `ordinal_suffix` as it adds relatively significant
    # overhead (+~10%)
    return str(n) + (
        "th" if (11 <= (n % 100) <= 13)
        else ("th", "st", "nd", "rd", "th")[min(n % 10, 4)]
    )
