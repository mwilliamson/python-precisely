try:
    from itertools import zip_longest
except ImportError:
    from itertools import izip_longest as zip_longest

from .base import Matcher
from .results import matched, unmatched, indented_list, indexed_indented_list
from .coercion import to_matcher


def contains_exactly(*matchers):
    return ContainsExactlyMatcher([to_matcher(matcher) for matcher in matchers])

class ContainsExactlyMatcher(Matcher):
    def __init__(self, matchers):
        self._matchers = matchers
    
    def match(self, actual):
        matches = _Matches(list(actual))
        for matcher in self._matchers:
            result = matches.match(matcher)
            if not result.is_match:
                return result
        return matches.match_remaining()
    
    def describe(self):
        return "iterable containing in any order:{0}".format(indented_list(
            matcher.describe()
            for matcher in self._matchers
        ))


class _Matches(object):
    def __init__(self, values):
        self._values = values
        self._is_matched = [False] * len(values)
    
    def match(self, matcher):
        mismatches = []
        for index, (is_matched, value) in enumerate(zip(self._is_matched, self._values)):
            if is_matched:
                result = unmatched("already matched")
            else:
                result = matcher.match(value)
                
            if result.is_match:
                self._is_matched[index] = True
                return result
            else:
                mismatches.append(result)
        
        return unmatched("was missing element:{0}\nmismatched elements:{1}".format(
            indented_list([matcher.describe()]),
            indented_list("{0}: {1}".format(repr(value), mismatch.explanation) for value, mismatch in zip(self._values, mismatches)),
        ))
    
    def match_remaining(self):
        if all(self._is_matched):
            return matched()
        else:
            return unmatched("had extra elements:{0}".format(indented_list(
                repr(value)
                for is_matched, value in zip(self._is_matched, self._values)
                if not is_matched
            )))


def is_same_sequence(*matchers):
    return IsSameSequenceMatcher([to_matcher(matcher) for matcher in matchers])


class IsSameSequenceMatcher(Matcher):
    _missing = object()
    
    def __init__(self, matchers):
        self._matchers = matchers
    
    def match(self, actual):
        values = list(actual)
        extra = []
        for index, (matcher, value) in enumerate(zip_longest(self._matchers, values, fillvalue=self._missing)):
            if matcher is self._missing:
                extra.append(value)
            elif value is self._missing:
                return unmatched("element at index {0} was missing".format(index))
            else:
                result = matcher.match(value)
                if not result.is_match:
                    return unmatched("element at index {0} mismatched:{1}".format(index, indented_list([result.explanation])))
        
        if extra:
            return unmatched("had extra elements:{0}".format(indented_list(map(repr, extra))))
        else:
            return matched()
    
    def describe(self):
        return "iterable containing in order:{0}".format(indexed_indented_list(
            matcher.describe()
            for matcher in self._matchers
        ))
