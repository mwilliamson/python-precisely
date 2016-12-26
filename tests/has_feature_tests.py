import collections

from nose.tools import istest, assert_equal

from precisely import has_feature, equal_to
from precisely.results import matched, unmatched


User = collections.namedtuple("User", ["username"])


@istest
def matches_when_feature_has_correct_value():
    matcher = has_feature("name", lambda user: user.username, equal_to("bob"))
    assert_equal(matched(), matcher.match(User("bob")))


@istest
def mismatches_when_feature_extraction_fails():
    # TODO:
    return
    matcher = has_feature("name", lambda user: user.username, equal_to("bob"))
    assert_equal(
        unmatched(""),
        matcher.match("bobbity")
    )


@istest
def explanation_of_mismatch_contains_mismatch_of_feature():
    matcher = has_feature("name", lambda user: user.username, equal_to("bob"))
    assert_equal(
        unmatched("name: was 'bobbity'"),
        matcher.match(User("bobbity"))
    )


@istest
def submatcher_is_coerced_to_matcher():
    matcher = has_feature("name", lambda user: user.username, "bob")
    assert_equal(
        unmatched("name: was 'bobbity'"),
        matcher.match(User("bobbity"))
    )


@istest
def description_contains_description_of_property():
    matcher = has_feature("name", lambda user: user.username, equal_to("bob"))
    assert_equal(
        "name: 'bob'",
        matcher.describe()
    )

