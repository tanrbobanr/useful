def mangle(name: str, cls: type) -> str:
    """Mangle the given `name` to the given `cls` (a type)."""
    cname = cls.__name__.strip("_")

    # handle exceptions
    if (
        not cname # class is only underscores
        or not name.startswith("__") # not a private variable
        or "." in name # contains a dot
        or name.endswith("__") # dunder name
    ):
        return name

    return f"_{cname}{name}"
