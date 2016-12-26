from .core_matchers import equal_to, anything, all_of
from .object_matchers import has_property, has_properties, instance_of
from .iterable_matchers import contains_exactly, is_same_sequence
from .feature_matchers import has_feature


def assert_that(value, matcher):
    result = matcher.match(value)
    if not result.is_match:
        raise AssertionError("\nExpected: {0}\nbut: {1}".format(matcher.describe(), result.explanation))
