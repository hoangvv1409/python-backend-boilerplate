from enum import Enum


def deep_get(dictionary, keys, default=None):
    from functools import reduce
    return reduce(
        lambda d, key: d.get(key, default) if isinstance(d, dict) else default,
        keys.split('.'), dictionary)


def clean_dict(obj):
    return {
        key: value for key, value in obj.items() if value
    }


def to_dict(obj, get_enum_value=True):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = to_dict(v, get_enum_value)

        return data
    elif hasattr(obj, "_ast"):
        return to_dict(obj._ast(), get_enum_value)
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [to_dict(v, get_enum_value) for v in obj]
    elif isinstance(obj, Enum):
        return obj.value if get_enum_value else obj
    elif hasattr(obj, "__dict__"):
        data = {}
        for key in dir(obj):
            if key.startswith('_'):
                continue

            attr = getattr(obj, key)
            if callable(attr):
                continue

            data[key] = to_dict(attr, get_enum_value)

        return data
    else:
        return obj
