def get_abc_registry(abc_class: abc.ABCMeta) -> weakref.WeakSet:
    """Get the ABC virtual subclass registry of the given ABC"""
    # if abc is using _py_abc, we can simply access _abc_registry
    registry: Union[weakref.WeakSet, None] = getattr(
        abc_class, "_abc_registry", None
    )
    if registry is not None:
        return registry

    # use _abc._get_dump to obtain registry
    # see https://github.com/search?q=repo%3Apython/cpython%20_abc__get_dump&type=code
    # for _abc._get_dump return structure
    return __import__("_abc")._get_dump(abc_class)[0]
