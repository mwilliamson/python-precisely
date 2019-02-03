from .base import Matcher
from .results import matched, unmatched


def raises(exception_matcher):
    return RaisesMatcher(exception_matcher)


class RaisesMatcher(Matcher):
    def __init__(self, exception_matcher):
        self._exception_matcher = exception_matcher

    def match(self, actual):
        try:
            actual()
        except Exception as error:
            result = self._exception_matcher.match(error)
            if result.is_match:
                return matched()
            else:
                return unmatched("exception did not match: {0}".format(result.explanation))

        return unmatched("did not raise exception")

    def describe(self):
        return "a function raising: {0}".format(self._exception_matcher.describe())
