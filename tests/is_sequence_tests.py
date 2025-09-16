from precisely import is_sequence, equal_to
from precisely.results import matched, unmatched
from .testing import assert_equal


def test_matches_when_all_submatchers_match_one_item_with_no_items_leftover():
    matcher = is_sequence(equal_to("apple"), equal_to("banana"))

    assert_equal(matched(), matcher.match(["apple", "banana"]))


def test_mismatches_when_actual_is_not_iterable():
    matcher = is_sequence(equal_to("apple"))

    assert_equal(
        unmatched("was not iterable\nwas 0"),
        matcher.match(0)
    )


def test_mismatches_when_items_are_in_wrong_order():
    matcher = is_sequence(equal_to("apple"), equal_to("banana"))

    assert_equal(
        unmatched("element at index 0 mismatched:\n * was 'banana'"),
        matcher.match(["banana", "apple"])
    )


def test_mismatches_when_item_is_missing():
    matcher = is_sequence(equal_to("apple"), equal_to("banana"), equal_to("coconut"))

    assert_equal(
        unmatched("element at index 2 was missing"),
        matcher.match(["apple", "banana"])
    )


def test_mismatches_when_item_is_expected_but_iterable_is_empty():
    matcher = is_sequence(equal_to("apple"))

    assert_equal(
        unmatched("iterable was empty"),
        matcher.match([])
    )


def test_when_empty_iterable_is_expected_then_empty_iterable_matches():
    matcher = is_sequence()

    assert_equal(
        matched(),
        matcher.match([])
    )


def test_mismatches_when_contains_extra_item():
    matcher = is_sequence(equal_to("apple"))

    assert_equal(
        unmatched("had extra elements:\n * 'coconut'"),
        matcher.match(["apple", "coconut"])
    )


def test_when_there_are_zero_submatchers_then_description_is_of_empty_iterable():
    matcher = is_sequence()

    assert_equal(
        "empty iterable",
        matcher.describe()
    )


def test_description_contains_descriptions_of_submatchers():
    matcher = is_sequence(equal_to("apple"), equal_to("banana"))

    assert_equal(
        "iterable containing in order:\n 0: 'apple'\n 1: 'banana'",
        matcher.describe()
    )


def test_elements_are_coerced_to_matchers():
    matcher = is_sequence("apple", "banana")

    assert_equal(
        "iterable containing in order:\n 0: 'apple'\n 1: 'banana'",
        matcher.describe()
    )

