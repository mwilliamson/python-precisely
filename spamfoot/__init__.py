from .results import matched, unmatched


def assert_that(value, matcher):
    result = matcher.match(value)
    if not result.is_match:
        raise AssertionError("Expected: {0}\nbut: {1}".format(matcher.describe(), result.explanation))


def equal_to(value):
    return EqualToMatcher(value)


class EqualToMatcher(object):
    def __init__(self, value):
        self._value = value
    
    def match(self, actual):
        if self._value == actual:
            return matched()
        else:
            return unmatched("was {0!r}".format(actual))
    
    def describe(self):
        return repr(self._value)


class AnyThingMatcher(object):
    def match(self, actual):
        return matched()
    
    def describe(self):
        return "anything"


anything = AnyThingMatcher()
