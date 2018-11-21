from nose.tools import istest, assert_equal

from precisely import all_elements, equal_to
from precisely.results import matched, unmatched


@istest
def matches_when_all_items_in_iterable_match():
    matcher = all_elements(equal_to("apple"))

    assert_equal(matched(), matcher.match(["apple", "apple"]))


@istest
def mismatches_when_item_in_iterable_does_not_match():
    matcher = all_elements(equal_to("apple"))

    assert_equal(
        unmatched("element at index 1 mismatched: was 'orange'"),
        matcher.match(["apple", "orange"])
    )


@istest
def matches_when_iterable_is_empty():
    matcher = all_elements(equal_to("apple"))

    assert_equal(matched(), matcher.match([]))


@istest
def description_contains_descriptions_of_submatcher():
    matcher = all_elements(equal_to("apple"))

    assert_equal(
        "all elements of iterable match: 'apple'",
        matcher.describe()
    )
