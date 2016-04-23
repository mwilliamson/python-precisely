import collections

from nose.tools import istest, assert_equal

from spamfoot import has_property, equal_to
from spamfoot.results import matched, unmatched


User = collections.namedtuple("User", ["username"])


@istest
def matches_when_property_has_correct_value():
    assert_equal(matched(), has_property("username", equal_to("bob")).match(User("bob")))


@istest
def mismatches_when_property_is_missing():
    assert_equal(
        unmatched("property username: missing"),
        has_property("username", equal_to("bob")).match("bobbity")
    )


@istest
def explanation_of_mismatch_contains_mismatch_of_property():
    assert_equal(
        unmatched("property username: was 'bobbity'"),
        has_property("username", equal_to("bob")).match(User("bobbity"))
    )


@istest
def submatcher_is_coerced_to_matcher():
    assert_equal(
        unmatched("property username: was 'bobbity'"),
        has_property("username", "bob").match(User("bobbity"))
    )


@istest
def description_contains_description_of_property():
    assert_equal(
        "property username: 'bob'",
        has_property("username", equal_to("bob")).describe()
    )

