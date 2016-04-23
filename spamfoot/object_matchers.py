from .results import matched, unmatched, indented_list
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


def has_properties(**matchers):
    return HasProperties(matchers)

class HasProperties(object):
    def __init__(self, matchers):
        self._matchers = [
            has_property(name, matcher)
            for name, matcher in matchers.items()
        ]
    
    def match(self, actual):
        for matcher in self._matchers:
            result = matcher.match(actual)
            if not result.is_match:
                return result
        return matched()
    
    def describe(self):
        return "properties:{0}".format(indented_list(
            "{0}: {1}".format(matcher._name, matcher._matcher.describe())
            for matcher in self._matchers
        ))
