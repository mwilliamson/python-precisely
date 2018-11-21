from nose.tools import istest, assert_equal

from precisely import equal_to, includes
from precisely.results import matched, unmatched


@istest
def matches_when_all_submatchers_match_one_item_with_no_items_leftover():
    matcher = includes(equal_to("apple"), equal_to("banana"))

    assert_equal(matched(), matcher.match(["apple", "banana"]))
    assert_equal(matched(), matcher.match(["apple", "banana", "coconut"]))


@istest
def mismatches_when_actual_is_not_iterable():
    matcher = includes(equal_to("apple"))

    assert_equal(
        unmatched("was not iterable\nwas 0"),
        matcher.match(0)
    )


@istest
def mismatches_when_item_is_missing():
    matcher = includes(equal_to("apple"), equal_to("banana"), equal_to("coconut"))

    assert_equal(
        unmatched("was missing element:\n  * 'banana'\nThese elements were in the iterable, but did not match the missing element:\n  * 'coconut': was 'coconut'\n  * 'apple': already matched"),
        matcher.match(["coconut", "apple"])
    )


@istest
def mismatches_when_duplicate_is_missing():
    matcher = includes(equal_to("apple"), equal_to("apple"))

    assert_equal(
        unmatched("was missing element:\n  * 'apple'\nThese elements were in the iterable, but did not match the missing element:\n  * 'apple': already matched"),
        matcher.match(["apple"])
    )


@istest
def matches_when_there_are_extra_items():
    matcher = includes(equal_to("apple"))

    assert_equal(matched(), matcher.match(["coconut", "apple"]))


@istest
def description_contains_descriptions_of_submatchers():
    matcher = includes(equal_to("apple"), equal_to("banana"))

    assert_equal(
        "iterable including elements:\n  * 'apple'\n  * 'banana'",
        matcher.describe()
    )


@istest
def elements_are_coerced_to_matchers():
    matcher = includes("apple", "banana")

    assert_equal(
        "iterable including elements:\n  * 'apple'\n  * 'banana'",
        matcher.describe()
    )

