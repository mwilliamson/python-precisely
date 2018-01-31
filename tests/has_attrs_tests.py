import collections

from nose.tools import istest, assert_equal

from precisely import has_attrs, equal_to
from precisely.results import matched, unmatched


User = collections.namedtuple("User", ["username", "email_address"])

@istest
def matches_when_properties_all_match():
    matcher = has_attrs(
        username=equal_to("bob"),
        email_address=equal_to("bob@example.com"),
    )
    
    assert_equal(matched(), matcher.match(User("bob", "bob@example.com")))


@istest
def mismatches_when_property_is_missing():
    matcher = has_attrs(
        ("username", equal_to("bob")),
        ("email_address", equal_to("bob@example.com")),
    )
    
    assert_equal(
        unmatched("was missing attribute username"),
        matcher.match("bobbity")
    )


@istest
def explanation_of_mismatch_contains_mismatch_of_property():
    matcher = has_attrs(
        username=equal_to("bob"),
        email_address=equal_to("bob@example.com"),
    )
    
    assert_equal(
        unmatched("attribute email_address was 'bobbity@example.com'"),
        matcher.match(User("bob", "bobbity@example.com"))
    )


@istest
def submatcher_is_coerced_to_matcher():
    matcher = has_attrs(username="bob")
    
    assert_equal(
        unmatched("attribute username was 'bobbity'"),
        matcher.match(User("bobbity", None))
    )


@istest
def description_contains_descriptions_of_properties():
    matcher = has_attrs(
        username=equal_to("bob"),
    )
    
    assert_equal(
        "object with attributes:\n  * username: 'bob'",
        matcher.describe()
    )


@istest
def can_pass_properties_as_list_of_tuples():
    matcher = has_attrs(
        ("username", equal_to("bob")),
        ("email_address", equal_to("bob@example.com")),
    )
    
    assert_equal(
        "object with attributes:\n  * username: 'bob'\n  * email_address: 'bob@example.com'",
        matcher.describe()
    )


@istest
def can_pass_properties_as_dictionary():
    matcher = has_attrs({
        "username": equal_to("bob"),
    })
    
    assert_equal(
        "object with attributes:\n  * username: 'bob'",
        matcher.describe()
    )
