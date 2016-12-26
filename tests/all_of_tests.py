import collections

from nose.tools import istest, assert_equal

from precisely import all_of, has_attr, equal_to
from precisely.results import matched, unmatched


User = collections.namedtuple("User", ["username", "email_address"])

@istest
def matches_when_submatchers_all_match():
    matcher = all_of(
        has_attr("username", equal_to("bob")),
        has_attr("email_address", equal_to("bob@example.com")),
    )
    
    assert_equal(matched(), matcher.match(User("bob", "bob@example.com")))


@istest
def mismatches_when_submatcher_mismatches():
    matcher = all_of(
        has_attr("username", equal_to("bob")),
        has_attr("email_address", equal_to("bob@example.com")),
    )
    
    assert_equal(
        unmatched("attribute username: missing"),
        matcher.match("bobbity")
    )


@istest
def description_contains_descriptions_of_submatchers():
    matcher = all_of(
        has_attr("username", equal_to("bob")),
        has_attr("email_address", equal_to("bob@example.com")),
    )
    
    assert_equal(
        "all of:\n  * attribute username: 'bob'\n  * attribute email_address: 'bob@example.com'",
        matcher.describe()
    )

