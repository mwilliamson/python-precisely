import collections

from precisely import all_of, has_attr, equal_to
from precisely.results import matched, unmatched
from .testing import assert_equal


User = collections.namedtuple("User", ["username", "email_address"])

def test_matches_when_submatchers_all_match():
    matcher = all_of(
        has_attr("username", equal_to("bob")),
        has_attr("email_address", equal_to("bob@example.com")),
    )

    assert_equal(matched(), matcher.match(User("bob", "bob@example.com")))


def test_mismatches_when_submatcher_mismatches():
    matcher = all_of(
        has_attr("username", equal_to("bob")),
        has_attr("email_address", equal_to("bob@example.com")),
    )

    assert_equal(
        unmatched("was missing attribute username"),
        matcher.match("bobbity")
    )


def test_description_contains_descriptions_of_submatchers():
    matcher = all_of(
        has_attr("username", equal_to("bob")),
        has_attr("email_address", equal_to("bob@example.com")),
    )

    assert_equal(
        "all of:\n * object with attribute username: 'bob'\n * object with attribute email_address: 'bob@example.com'",
        matcher.describe()
    )

