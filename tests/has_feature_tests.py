import collections


from precisely import has_feature, equal_to
from precisely.results import matched, unmatched


User = collections.namedtuple("User", ["username"])


def test_matches_when_feature_has_correct_value():
    matcher = has_feature("name", lambda user: user.username, equal_to("bob"))
    assert matched() == matcher.match(User("bob"))


def test_mismatches_when_feature_extraction_fails():
    # TODO:
    return
    matcher = has_feature("name", lambda user: user.username, equal_to("bob"))
    assert unmatched("") == matcher.match("bobbity")


def test_explanation_of_mismatch_contains_mismatch_of_feature():
    matcher = has_feature("name", lambda user: user.username, equal_to("bob"))
    assert unmatched("name: was 'bobbity'") == matcher.match(User("bobbity"))


def test_submatcher_is_coerced_to_matcher():
    matcher = has_feature("name", lambda user: user.username, "bob")
    assert unmatched("name: was 'bobbity'") == matcher.match(User("bobbity"))


def test_description_contains_description_of_property():
    matcher = has_feature("name", lambda user: user.username, equal_to("bob"))
    assert "name: 'bob'" == matcher.describe()

