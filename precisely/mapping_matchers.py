from .base import Matcher
from .coercion import to_matcher
from .results import matched, unmatched, indented_list


def is_mapping(matchers):
    return IsMappingMatcher(dict(
        (key, to_matcher(matcher))
        for key, matcher in matchers.items()
    ))


class IsMappingMatcher(Matcher):
    def __init__(self, matchers):
        self._matchers = matchers

    def match(self, actual):
        undefined = object()
        for key, matcher in self._matchers.items():
            value = actual.get(key, undefined)
            if value is undefined:
                return unmatched("was missing key: {0!r}".format(key))

            value_result = matcher.match(value)
            if not value_result.is_match:
                return unmatched("value for key {0!r} mismatched:{1}".format(key, indented_list([value_result.explanation])))

        extra_keys = set(actual.keys()) - set(self._matchers.keys())
        if extra_keys:
            return unmatched("had extra keys:{0}".format(indented_list(sorted(map(repr, extra_keys)))))

        return matched()

    def describe(self):
        return "mapping with items:{0}".format(indented_list(sorted(
            "{0!r}: {1}".format(key, matcher.describe())
            for key, matcher in self._matchers.items()
        )))
