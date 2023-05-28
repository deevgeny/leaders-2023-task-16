def set_attrs_from_dict(obj: object, d: dict[str, any]):
    for key, val in d.items():
        setattr(obj, key, val)
