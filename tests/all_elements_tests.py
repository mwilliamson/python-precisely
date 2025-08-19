from asserts import assert_equal

from precisely import all_elements, equal_to
from precisely.results import matched, unmatched


def test_matches_when_all_items_in_iterable_match():
    matcher = all_elements(equal_to("apple"))

    assert_equal(matched(), matcher.match(["apple", "apple"]))


def test_mismatches_when_actual_is_not_iterable():
    matcher = all_elements(equal_to("apple"))
    
    assert_equal(unmatched("was not iterable\nwas 0"), matcher.match(0))


def test_mismatches_when_item_in_iterable_does_not_match():
    matcher = all_elements(equal_to("apple"))

    assert_equal(unmatched("element at index 1 mismatched: was 'orange'"), matcher.match(["apple", "orange"]))


def test_matches_when_iterable_is_empty():
    matcher = all_elements(equal_to("apple"))

    assert_equal(matched(), matcher.match([]))


def test_description_contains_descriptions_of_submatcher():
    matcher = all_elements(equal_to("apple"))

    assert_equal("all elements of iterable match: 'apple'", matcher.describe())
