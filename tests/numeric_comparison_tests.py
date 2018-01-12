from nose.tools import istest, assert_equal

from precisely import greater_than
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
