import collections

from nose.tools import istest, assert_equal

from precisely import any_of, has_attr, equal_to
from precisely.results import matched, unmatched


User = collections.namedtuple("User", ["username", "email_address"])

@istest
def matches_when_submatchers_all_match():
    matcher = any_of(
        has_attr("username", equal_to("bob")),
        has_attr("email_address", equal_to("bob@example.com")),
    )
    
    assert_equal(matched(), matcher.match(User("bob", "bob@example.com")))


@istest
def matches_when_any_submatchers_match():
    matcher = any_of(
        equal_to("bob"),
        equal_to("jim"),
    )
    
    assert_equal(
        matched(),
        matcher.match("bob"),
    )


@istest
def mismatches_when_no_submatchers_match():
    matcher = any_of(
        equal_to("bob"),
        equal_to("jim"),
    )
    
    assert_equal(
        unmatched("did not match any of:\n * 'bob' [was 'alice']\n * 'jim' [was 'alice']"),
        matcher.match("alice"),
    )


@istest
def description_contains_descriptions_of_submatchers():
    matcher = any_of(
        has_attr("username", equal_to("bob")),
        has_attr("email_address", equal_to("bob@example.com")),
    )
    
    assert_equal(
        "any of:\n * object with attribute username: 'bob'\n * object with attribute email_address: 'bob@example.com'",
        matcher.describe()
    )

