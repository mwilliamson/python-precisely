from precisely import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to
from precisely.results import matched, unmatched


def test_greater_than_matches_when_actual_is_greater_than_value():
    matcher = greater_than(42)
    assert matched() == matcher.match(43)
    assert unmatched("was 42") == matcher.match(42)
    assert unmatched("was 41") == matcher.match(41)


def test_greater_than_description_describes_value():
    matcher = greater_than(42)
    assert matcher.describe() == "greater than 42"

def test_greater_than_or_equal_to_matches_when_actual_is_greater_than_or_equal_to_value():
    matcher = greater_than_or_equal_to(42)
    assert matched() == matcher.match(43)
    assert matched() == matcher.match(42)
    assert unmatched("was 41") == matcher.match(41)


def test_greater_than_or_equal_to_description_describes_value():
    matcher = greater_than_or_equal_to(42)
    assert matcher.describe() == "greater than or equal to 42"


def test_less_than_matches_when_actual_is_less_than_value():
    matcher = less_than(42)
    assert matched() == matcher.match(41)
    assert unmatched("was 42") == matcher.match(42)
    assert unmatched("was 43") == matcher.match(43)


def test_less_than_description_describes_value():
    matcher = less_than(42)
    assert matcher.describe() == "less than 42"


def test_less_than_or_equal_to_matches_when_actual_is_less_than_or_equal_to_value():
    matcher = less_than_or_equal_to(42)
    assert matched() == matcher.match(41)
    assert matched() == matcher.match(42)
    assert unmatched("was 43") == matcher.match(43)


def test_less_than_or_equal_to_description_describes_value():
    matcher = less_than_or_equal_to(42)
    assert matcher.describe() == "less than or equal to 42"