from nose.tools import istest, assert_equal

from precisely import equal_to, mapping_includes
from precisely.results import matched, unmatched


@istest
def matches_when_keys_and_values_match():
    matcher = mapping_includes({"a": equal_to(1), "b": equal_to(2)})
    assert_equal(matched(), matcher.match({"a": 1, "b": 2}))


@istest
def values_are_coerced_to_matchers():
    matcher = mapping_includes({"a": 1, "b": 2})
    assert_equal(matched(), matcher.match({"a": 1, "b": 2}))


@istest
def does_not_match_when_value_does_not_match():
    matcher = mapping_includes({"a": equal_to(1), "b": equal_to(2)})
    assert_equal(
        unmatched("value for key 'b' mismatched:\n * was 3"),
        matcher.match({"a": 1, "b": 3, "c": 4}),
    )


@istest
def does_not_match_when_keys_are_missing():
    matcher = mapping_includes({"a": equal_to(1), "b": equal_to(2)})
    assert_equal(unmatched("was missing key: 'b'"), matcher.match({"a": 1}))


@istest
def matches_when_there_are_extra_keys():
    matcher = mapping_includes({"a": equal_to(1)})
    assert_equal(matched(), matcher.match({"a": 1, "b": 1, "c": 1}))


@istest
def description_describes_keys_and_value_matchers():
    matcher = mapping_includes({"a": equal_to(1), "b": equal_to(2)})
    assert_equal("mapping including items:\n * 'a': 1\n * 'b': 2", matcher.describe())
