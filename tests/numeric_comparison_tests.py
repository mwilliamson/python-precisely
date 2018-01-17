from nose.tools import istest, assert_equal

from precisely import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, close_to
from precisely.results import matched, unmatched


@istest
def greater_than_matches_when_actual_is_greater_than_value():
    matcher = greater_than(42)
    assert_equal(matched(), matcher.match(43))
    assert_equal(unmatched("was 42"), matcher.match(42))
    assert_equal(unmatched("was 41"), matcher.match(41))


@istest
def greater_than_description_describes_value():
    matcher = greater_than(42)
    assert_equal("greater than 42", matcher.describe())


@istest
def greater_than_or_equal_to_matches_when_actual_is_greater_than_or_equal_to_value():
    matcher = greater_than_or_equal_to(42)
    assert_equal(matched(), matcher.match(43))
    assert_equal(matched(), matcher.match(42))
    assert_equal(unmatched("was 41"), matcher.match(41))


@istest
def greater_than_or_equal_to_description_describes_value():
    matcher = greater_than_or_equal_to(42)
    assert_equal("greater than or equal to 42", matcher.describe())


@istest
def less_than_matches_when_actual_is_less_than_value():
    matcher = less_than(42)
    assert_equal(matched(), matcher.match(41))
    assert_equal(unmatched("was 42"), matcher.match(42))
    assert_equal(unmatched("was 43"), matcher.match(43))


@istest
def less_than_description_describes_value():
    matcher = less_than(42)
    assert_equal("less than 42", matcher.describe())


@istest
def less_than_or_equal_to_matches_when_actual_is_less_than_or_equal_to_value():
    matcher = less_than_or_equal_to(42)
    assert_equal(matched(), matcher.match(41))
    assert_equal(matched(), matcher.match(42))
    assert_equal(unmatched("was 43"), matcher.match(43))


@istest
def less_than_or_equal_to_description_describes_value():
    matcher = less_than_or_equal_to(42)
    assert_equal("less than or equal to 42", matcher.describe())


@istest
def close_to_matches_when_actual_is_close_to_value_plus_delta():
    matcher = close_to(42, 1)
    assert_equal(matched(), matcher.match(43))
    assert_equal(matched(), matcher.match(41))
    assert_equal(unmatched("was 40"), matcher.match(40))


@istest
def close_to_description_describes_value():
    matcher = close_to(42, 1)
    assert_equal("close to 42 +/- 1", matcher.describe())
