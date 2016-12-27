from .base import Matcher, is_matcher
from .core_matchers import equal_to, anything, all_of, any_of
from .object_matchers import has_attr, has_attrs, instance_of
from .iterable_matchers import contains_exactly, is_same_sequence
from .feature_matchers import has_feature


__all__ = [
    "assert_that",
    "Matcher",
    "is_matcher",
    "equal_to",
    "anything",
    "all_of",
    "any_of",
    "has_attr",
    "has_attrs",
    "instance_of",
    "contains_exactly",
    "is_same_sequence",
    "has_feature",
]


def assert_that(value, matcher):
    result = matcher.match(value)
    if not result.is_match:
        raise AssertionError("\nExpected: {0}\nbut: {1}".format(matcher.describe(), result.explanation))
