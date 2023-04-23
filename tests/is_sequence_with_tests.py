from nose.tools import istest, assert_equal

from precisely import is_sequence_with, equal_to
from precisely.results import matched, unmatched


@istest
def matches_when_all_submatchers_match_one_item_with_no_items_leftover():
    matcher = is_sequence_with(equal_to("apple"), equal_to("banana"))

    assert_equal(matched(), matcher.match(["apple", "banana"]))


@istest
def mismatches_when_actual_is_not_iterable():
    matcher = is_sequence_with(equal_to("apple"))

    assert_equal(
        unmatched("was not iterable\nwas 0"),
        matcher.match(0)
    )


@istest
def mismatches_when_items_are_in_wrong_order():
    matcher = is_sequence_with(equal_to("apple"), equal_to("banana"))

    assert_equal(
        unmatched("element at index 0 mismatched:\n * was 'banana'"),
        matcher.match(["banana", "apple"])
    )


@istest
def mismatches_when_item_is_missing():
    matcher = is_sequence_with(equal_to("apple"), equal_to("banana"), equal_to("coconut"))

    assert_equal(
        unmatched("element at index 2 was missing"),
        matcher.match(["apple", "banana"])
    )


@istest
def mismatches_when_item_is_expected_but_iterable_is_empty():
    matcher = is_sequence_with(equal_to("apple"))

    assert_equal(
        unmatched("iterable was empty"),
        matcher.match([])
    )


@istest
def when_empty_iterable_is_expected_then_empty_iterable_matches():
    matcher = is_sequence_with()

    assert_equal(
        matched(),
        matcher.match([])
    )


@istest
def matches_when_contains_extra_item_after():
    matcher = is_sequence_with(equal_to("apple"), equal_to("pear"))

    assert_equal(
        matched(),
        matcher.match(["apple", "pear", "coconut"])
    )


@istest
def matches_when_contains_extra_item_before():
    matcher = is_sequence_with(equal_to("apple"), equal_to("pear"))

    assert_equal(
        matched(),
        matcher.match(["coconut", "apple", "pear"])
    )


@istest
def when_there_are_zero_submatchers_then_description_is_of_empty_iterable():
    matcher = is_sequence_with()

    assert_equal(
        "empty iterable",
        matcher.describe()
    )


@istest
def description_contains_descriptions_of_submatchers():
    matcher = is_sequence_with(equal_to("apple"), equal_to("banana"))

    assert_equal(
        "iterable containing in order:\n 0: 'apple'\n 1: 'banana'",
        matcher.describe()
    )


@istest
def elements_are_coerced_to_matchers():
    matcher = is_sequence_with("apple", "banana")

    assert_equal(
        "iterable containing in order:\n 0: 'apple'\n 1: 'banana'",
        matcher.describe()
    )
