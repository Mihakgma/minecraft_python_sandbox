import collections


# import sys


def flatten(l, seen=set()):
    for e in l:
        # Проверка на наличие циклической ссылки
        if id(e) in seen:
            continue
        seen.add(id(e))

        if isinstance(e, collections.abc.Iterable) and not any(isinstance(ee, collections.abc.Iterable) for ee in e):
            yield e
        elif isinstance(e, collections.abc.Iterable):
            for ee in flatten(e, seen): yield ee
        else:
            yield e


def flatten_parameters_to_bytestring(l):
    return b",".join(map(_misc_to_bytes, flatten(l)))


def _misc_to_bytes(m):
    """
    Convert an arbitrary object into a string encoded as a CP437 series of bytes.

    See `Connection.send` for more details.
    """
    return str(m).encode("utf-8")
