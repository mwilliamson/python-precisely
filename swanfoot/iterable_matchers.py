from .results import matched, unmatched, indented_list
from .coercion import to_matcher


def contains_exactly(*matchers):
    return ContainsExactlyMatcher([to_matcher(matcher) for matcher in matchers])

class ContainsExactlyMatcher(object):
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
        self._matched = [False] * len(values)
    
    def match(self, matcher):
        mismatches = []
        for index, (matched, value) in enumerate(zip(self._matched, self._values)):
            if matched:
                result = unmatched("already matched")
            else:
                result = matcher.match(value)
                
            if result.is_match:
                self._matched[index] = True
                return result
            else:
                mismatches.append(result)
        
        return unmatched("was missing element:{0}\nmismatched elements:{1}".format(
            indented_list([matcher.describe()]),
            indented_list("{0}: {1}".format(repr(value), mismatch.explanation) for value, mismatch in zip(self._values, mismatches)),
        ))
    
    def match_remaining(self):
        if all(self._matched):
            return matched()
        else:
            return unmatched("had extra elements:{0}".format(indented_list(
                repr(value)
                for matched, value in zip(self._matched, self._values)
                if not matched
            )))
