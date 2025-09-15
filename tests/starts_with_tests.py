from precisely import starts_with
from precisely.results import matched, unmatched


def test_starts_with_matches_when_actual_string_starts_with_value_passed_to_matcher():
    matcher = starts_with("ab")
    assert matched() == matcher.match("ab")
    assert matched() == matcher.match("abc")
    assert matched() == matcher.match("abcd")
    assert unmatched("was 'a'") == matcher.match("a")
    assert unmatched("was 'cab'") == matcher.match("cab")


def test_starts_with_description_describes_value():
    matcher = starts_with("ab")
    assert "starts with 'ab'" == matcher.describe()