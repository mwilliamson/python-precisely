from .base import Matcher
from .results import matched, unmatched


def raises(exception):
    return RaisesMatcher(exception)


class RaisesMatcher(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def match(self, actual):
        try:
            try:
                actual()
            except self._expected:
                return matched()
        except Exception as e:
            return unmatched("raised {0!r}".format(e.__class__.__name__))

        return unmatched("no exception raised")

    def describe(self):
        return "expected {0}".format(self._expected)
