import collections

from nose.tools import istest, assert_equal

from precisely import has_attr, equal_to
from precisely.results import matched, unmatched


User = collections.namedtuple("User", ["username"])


@istest
def matches_when_property_has_correct_value():
    assert_equal(matched(), has_attr("username", equal_to("bob")).match(User("bob")))


@istest
def mismatches_when_property_is_missing():
    assert_equal(
        unmatched("attribute username: missing"),
        has_attr("username", equal_to("bob")).match("bobbity")
    )


@istest
def explanation_of_mismatch_contains_mismatch_of_property():
    assert_equal(
        unmatched("attribute username: was 'bobbity'"),
        has_attr("username", equal_to("bob")).match(User("bobbity"))
    )


@istest
def submatcher_is_coerced_to_matcher():
    assert_equal(
        unmatched("attribute username: was 'bobbity'"),
        has_attr("username", "bob").match(User("bobbity"))
    )


@istest
def description_contains_description_of_property():
    assert_equal(
        "attribute username: 'bob'",
        has_attr("username", equal_to("bob")).describe()
    )

