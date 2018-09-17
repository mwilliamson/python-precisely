from nose.tools import istest, assert_equal

from precisely import contains_only, equal_to
from precisely.results import matched, unmatched


@istest
def matches_when_all_items_in_iterable_match():
    matcher = contains_only(equal_to("apple"))

    assert_equal(matched(), matcher.match(["apple", "apple"]))


@istest
def mismatches_when_item_in_iterable_does_not_match():
    matcher = contains_only(equal_to("apple"))

    assert_equal(
        unmatched("element at index 1 mismatched: was 'orange'"),
        matcher.match(["apple", "orange"])
    )


@istest
def mismatches_when_iterable_is_empty():
    matcher = contains_only(equal_to("apple"))

    assert_equal(
        unmatched("empty iterable"),
        matcher.match([])
    )


@istest
def description_contains_descriptions_of_submatcher():
    matcher = contains_only(equal_to("apple"))

    assert_equal(
        "iterable only containing: 'apple'",
        matcher.describe()
    )
