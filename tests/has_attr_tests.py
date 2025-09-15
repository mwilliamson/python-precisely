import collections


from precisely import has_attr, equal_to
from precisely.results import matched, unmatched


User = collections.namedtuple("User", ["username"])


def test_matches_when_property_has_correct_value():
    assert matched() == has_attr("username", equal_to("bob")).match(User("bob"))


def test_mismatches_when_property_is_missing():
    assert unmatched("was missing attribute username") == has_attr("username", equal_to("bob")).match("bobbity")


def test_explanation_of_mismatch_contains_mismatch_of_property():
    assert unmatched("attribute username was 'bobbity'") == has_attr("username", equal_to("bob")).match(User("bobbity"))


def test_submatcher_is_coerced_to_matcher():
    assert unmatched("attribute username was 'bobbity'") == has_attr("username", "bob").match(User("bobbity"))


def test_description_contains_description_of_property():
    assert "object with attribute username: 'bob'" == has_attr("username", equal_to("bob")).describe()

