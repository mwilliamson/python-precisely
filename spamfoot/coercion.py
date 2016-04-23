from .core_matchers import equal_to


def to_matcher(value):
    if _is_matcher(value):
        return value
    else:
        return equal_to(value)


def _is_matcher(value):
    return callable(getattr(value, "describe", None)) and callable(getattr(value, "match", None))
