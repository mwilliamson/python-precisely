import collections

from nose.tools import istest, assert_equal

from swanfoot import has_properties, equal_to
from swanfoot.results import matched, unmatched


User = collections.namedtuple("User", ["username", "email_address"])

@istest
def matches_when_properties_all_match():
    matcher = has_properties(
        username=equal_to("bob"),
        email_address=equal_to("bob@example.com"),
    )
    
    assert_equal(matched(), matcher.match(User("bob", "bob@example.com")))


@istest
def mismatches_when_property_is_missing():
    matcher = has_properties(
        ("username", equal_to("bob")),
        ("email_address", equal_to("bob@example.com")),
    )
    
    assert_equal(
        unmatched("property username: missing"),
        matcher.match("bobbity")
    )


@istest
def explanation_of_mismatch_contains_mismatch_of_property():
    matcher = has_properties(
        username=equal_to("bob"),
        email_address=equal_to("bob@example.com"),
    )
    
    assert_equal(
        unmatched("property email_address: was 'bobbity@example.com'"),
        matcher.match(User("bob", "bobbity@example.com"))
    )


@istest
def submatcher_is_coerced_to_matcher():
    matcher = has_properties(username="bob")
    
    assert_equal(
        unmatched("property username: was 'bobbity'"),
        matcher.match(User("bobbity", None))
    )


@istest
def description_contains_descriptions_of_properties():
    matcher = has_properties(
        username=equal_to("bob"),
    )
    
    assert_equal(
        "properties:\n  * username: 'bob'",
        matcher.describe()
    )


@istest
def can_pass_properties_as_list_of_tuples():
    matcher = has_properties(
        ("username", equal_to("bob")),
        ("email_address", equal_to("bob@example.com")),
    )
    
    assert_equal(
        "properties:\n  * username: 'bob'\n  * email_address: 'bob@example.com'",
        matcher.describe()
    )


@istest
def can_pass_properties_as_dictionary():
    matcher = has_properties({
        "username": equal_to("bob"),
    })
    
    assert_equal(
        "properties:\n  * username: 'bob'",
        matcher.describe()
    )
