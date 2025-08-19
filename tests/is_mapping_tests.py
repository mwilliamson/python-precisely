from nose.tools import assert_equal

from precisely import equal_to, is_mapping
from precisely.results import matched, unmatched


def test_matches_when_keys_and_values_match():
    matcher = is_mapping({"a": equal_to(1), "b": equal_to(2)})
    assert_equal(matched(), matcher.match({"a": 1, "b": 2}))


def test_values_are_coerced_to_matchers():
    matcher = is_mapping({"a": 1, "b": 2})
    assert_equal(matched(), matcher.match({"a": 1, "b": 2}))


def test_does_not_match_when_value_does_not_match():
    matcher = is_mapping({"a": equal_to(1), "b": equal_to(2)})
    assert_equal(unmatched("value for key 'b' mismatched:\n * was 3"), matcher.match({"a": 1, "b": 3}))


def test_does_not_match_when_keys_are_missing():
    matcher = is_mapping({"a": equal_to(1), "b": equal_to(2)})
    assert_equal(unmatched("was missing key: 'b'"), matcher.match({"a": 1}))


def test_does_not_match_when_there_are_extra_keys():
    matcher = is_mapping({"a": equal_to(1)})
    assert_equal(unmatched("had extra keys:\n * 'b'\n * 'c'"), matcher.match({"a": 1, "b": 1, "c": 1}))


def test_description_describes_keys_and_value_matchers():
    matcher = is_mapping({"a": equal_to(1), "b": equal_to(2)})
    assert_equal("mapping with items:\n * 'a': 1\n * 'b': 2", matcher.describe())
