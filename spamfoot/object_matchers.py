from .results import matched, unmatched
from .coercion import to_matcher


def has_property(name, matcher):
    return HasProperty(name, to_matcher(matcher))


class HasProperty(object):
    def __init__(self, name, matcher):
        self._name = name
        self._matcher = matcher
    
    def match(self, actual):
        if not hasattr(actual, self._name):
            return unmatched(self._description("missing"))
        else:
            actual_property = getattr(actual, self._name)
            property_result = self._matcher.match(actual_property)
            if property_result.is_match:
                return matched()
            else:
                return unmatched(self._description(property_result.explanation))
    
    def describe(self):
        return self._description(self._matcher.describe())
    
    def _description(self, value):
        return "property {0}: {1}".format(self._name, value)
