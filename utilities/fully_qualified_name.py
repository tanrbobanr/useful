def fqn(tp: type, show_builtin: bool = False):
    """Get the fully-qualified name of type `tp`. This can be either a
    conventional type (such as those defined with `class`), or a
    function. Builtin types do no get displayed with `builtin.` unless
    the `show_builtin` parameter is `True`.

    Example
    -------
    ```
    >>> from multiprocessing import context
    >>> fqn(context.BaseContext)
    multiprocessing.context.BaseContext
    >>> fqn(str.strip)
    str.strip
    ```
    """
    # possibly a method
    if not hasattr(tp, "__module__"):
        objcls = getattr(tp, "__objclass__", None)

        # no parent class
        if not objcls:
            return getattr(tp, "__qualname__", tp.__name__)
        
        # set tp to parent class
        append = f".{tp.__name__}"
        tp = objcls
    else:
        append = ""

    mod = tp.__module__

    # __module__ is allowed to be None; skip module if its part of
    # builtins unless show_builtin=True
    if not show_builtin and (not mod or mod == "builtins"):
        return f"{tp.__qualname__}{append}"
    return f"{mod}.{tp.__qualname__}{append}"
