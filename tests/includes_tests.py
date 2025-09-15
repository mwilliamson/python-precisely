
from precisely import equal_to, includes
from precisely.results import matched, unmatched


def test_matches_when_all_submatchers_match_one_item_with_no_items_leftover():
    matcher = includes(equal_to("apple"), equal_to("banana"))

    assert matched() == matcher.match(["apple", "banana"])
    assert matched() == matcher.match(["apple", "banana", "coconut"])


def test_mismatches_when_actual_is_not_iterable():
    matcher = includes(equal_to("apple"))

    assert unmatched("was not iterable\nwas 0") == matcher.match(0)


def test_mismatches_when_item_is_missing():
    matcher = includes(equal_to("apple"), equal_to("banana"), equal_to("coconut"))

    assert unmatched("was missing element:\n * 'banana'\nThese elements were in the iterable, but did not match the missing element:\n * 'coconut': was 'coconut'\n * 'apple': already matched") == matcher.match(["coconut", "apple"])


def test_mismatches_when_duplicate_is_missing():
    matcher = includes(equal_to("apple"), equal_to("apple"))

    assert unmatched("was missing element:\n * 'apple'\nThese elements were in the iterable, but did not match the missing element:\n * 'apple': already matched") == matcher.match(["apple"])


def test_mismatches_when_item_is_expected_but_iterable_is_empty():
    matcher = includes(equal_to("apple"))

    assert unmatched("iterable was empty") == matcher.match([])


def test_when_no_elements_are_expected_then_empty_iterable_matches():
    matcher = includes()

    assert matched() == matcher.match([])


def test_matches_when_there_are_extra_items():
    matcher = includes(equal_to("apple"))

    assert matched() == matcher.match(["coconut", "apple"])


def test_description_contains_descriptions_of_submatchers():
    matcher = includes(equal_to("apple"), equal_to("banana"))

    assert "iterable including elements:\n * 'apple'\n * 'banana'" == matcher.describe()


def test_elements_are_coerced_to_matchers():
    matcher = includes("apple", "banana")

    assert "iterable including elements:\n * 'apple'\n * 'banana'" == matcher.describe()

