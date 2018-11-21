from nose.tools import istest, assert_equal

from precisely import contains_exactly, equal_to
from precisely.results import matched, unmatched


@istest
def matches_when_all_submatchers_match_one_item_with_no_items_leftover():
    matcher = contains_exactly(equal_to("apple"), equal_to("banana"))
    
    assert_equal(matched(), matcher.match(["banana", "apple"]))


@istest
def mismatches_when_actual_is_not_iterable():
    matcher = contains_exactly()
    
    assert_equal(
        unmatched("was not iterable\nwas 0"),
        matcher.match(0)
    )


@istest
def mismatches_when_item_is_missing():
    matcher = contains_exactly(equal_to("apple"), equal_to("banana"), equal_to("coconut"))
    
    assert_equal(
        unmatched("was missing element:\n * 'banana'\nThese elements were in the iterable, but did not match the missing element:\n * 'coconut': was 'coconut'\n * 'apple': already matched"),
        matcher.match(["coconut", "apple"])
    )


@istest
def mismatches_when_item_is_expected_but_iterable_is_empty():
    matcher = contains_exactly(equal_to("apple"))

    assert_equal(
        unmatched("iterable was empty"),
        matcher.match([])
    )


@istest
def when_empty_iterable_is_expected_then_empty_iterable_matches():
    matcher = contains_exactly()

    assert_equal(
        matched(),
        matcher.match([])
    )


@istest
def mismatches_when_duplicate_is_missing():
    matcher = contains_exactly(equal_to("apple"), equal_to("apple"))
    
    assert_equal(
        unmatched("was missing element:\n * 'apple'\nThese elements were in the iterable, but did not match the missing element:\n * 'apple': already matched"),
        matcher.match(["apple"])
    )


@istest
def mismatches_when_contains_extra_item():
    matcher = contains_exactly(equal_to("apple"))
    
    assert_equal(
        unmatched("had extra elements:\n * 'coconut'"),
        matcher.match(["coconut", "apple"])
    )


@istest
def description_is_of_empty_iterable_when_there_are_zero_submatchers():
    matcher = contains_exactly()

    assert_equal("empty iterable", matcher.describe())


@istest
def description_uses_singular_when_there_is_one_submatcher():
    matcher = contains_exactly(equal_to("apple"))

    assert_equal(
        "iterable containing 1 element:\n * 'apple'",
        matcher.describe()
    )


@istest
def description_contains_descriptions_of_submatchers():
    matcher = contains_exactly(equal_to("apple"), equal_to("banana"))
    
    assert_equal(
        "iterable containing these 2 elements in any order:\n * 'apple'\n * 'banana'",
        matcher.describe()
    )


@istest
def elements_are_coerced_to_matchers():
    matcher = contains_exactly("apple", "banana")
    
    assert_equal(
        "iterable containing these 2 elements in any order:\n * 'apple'\n * 'banana'",
        matcher.describe()
    )

