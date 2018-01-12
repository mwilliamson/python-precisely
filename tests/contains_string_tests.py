from nose.tools import istest, assert_equal

from precisely import contains_string
from precisely.results import matched, unmatched


@istest
def contains_string_matches_when_actual_string_contains_value_passed_to_matcher():
    matcher = contains_string("ab")
    assert_equal(matched(), matcher.match("ab"))
    assert_equal(matched(), matcher.match("abc"))
    assert_equal(matched(), matcher.match("abcd"))
    assert_equal(matched(), matcher.match("cabd"))
    assert_equal(matched(), matcher.match("cdab"))
    assert_equal(unmatched("was 'a'"), matcher.match("a"))


@istest
def contains_string_description_describes_value():
    matcher = contains_string("ab")
    assert_equal("contains the string 'ab'", matcher.describe())
