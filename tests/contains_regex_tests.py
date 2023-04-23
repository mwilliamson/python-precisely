from nose.tools import istest, assert_equal

from precisely import contains_regex
from precisely.results import matched, unmatched


@istest
def contains_regex_matches_when_actual_string_matches_regex_pattern_passed_to_matcher():
    matcher = contains_regex(".*[Hh]ello$")

    assert_equal(matched(), matcher.match("hello"))
    assert_equal(matched(), matcher.match("Hello"))
    assert_equal(matched(), matcher.match("why hello"))
    assert_equal(unmatched("was 'why hello there'"), matcher.match("why hello there"))


@istest
def contains_regex_description_describes_value():
    matcher = contains_regex(".*")

    assert_equal("contains the regex pattern '.*'", matcher.describe())
