import collections

from nose.tools import istest, assert_equal

from swanfoot import contains_exactly, equal_to
from swanfoot.results import matched, unmatched


@istest
def matches_when_all_submatchers_match_one_item_with_no_items_leftover():
    matcher = contains_exactly(equal_to("apple"), equal_to("banana"))
    
    assert_equal(matched(), matcher.match(["banana", "apple"]))


@istest
def mismatches_when_item_is_missing():
    matcher = contains_exactly(equal_to("apple"), equal_to("banana"), equal_to("coconut"))
    
    assert_equal(
        unmatched("was missing element:\n  * 'banana'\nmismatched elements:\n  * 'coconut': was 'coconut'\n  * 'apple': already matched"),
        matcher.match(["coconut", "apple"])
    )


@istest
def mismatches_when_duplicate_is_missing():
    matcher = contains_exactly(equal_to("apple"), equal_to("apple"))
    
    assert_equal(
        unmatched("was missing element:\n  * 'apple'\nmismatched elements:\n  * 'apple': already matched"),
        matcher.match(["apple"])
    )


@istest
def mismatches_when_contains_extra_item():
    matcher = contains_exactly(equal_to("apple"))
    
    assert_equal(
        unmatched("had extra elements:\n  * 'coconut'"),
        matcher.match(["coconut", "apple"])
    )


@istest
def description_contains_descriptions_of_submatchers():
    matcher = contains_exactly(equal_to("apple"), equal_to("banana"))
    
    assert_equal(
        "iterable containing in any order:\n  * 'apple'\n  * 'banana'",
        matcher.describe()
    )


@istest
def elements_are_coerced_to_matchers():
    matcher = contains_exactly("apple", "banana")
    
    assert_equal(
        "iterable containing in any order:\n  * 'apple'\n  * 'banana'",
        matcher.describe()
    )

