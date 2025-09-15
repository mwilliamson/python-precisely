from precisely import contains_string
from precisely.results import matched, unmatched


def test_contains_string_matches_when_actual_string_contains_value_passed_to_matcher():
    matcher = contains_string("ab")
    assert matched() == matcher.match("ab")
    assert matched() == matcher.match("abc")
    assert matched() == matcher.match("abcd")
    assert matched() == matcher.match("cabd")
    assert matched() == matcher.match("cdab")
    assert unmatched("was 'a'") == matcher.match("a")


def test_contains_string_description_describes_value():
    matcher = contains_string("ab")
    assert matcher.describe() == "contains the string 'ab'"