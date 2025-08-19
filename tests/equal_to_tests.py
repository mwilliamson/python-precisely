from asserts import assert_equal

from precisely import equal_to
from precisely.results import matched, unmatched


def test_matches_when_values_are_equal():
    assert_equal(matched(), equal_to(1).match(1))


def test_explanation_of_mismatch_contains_repr_of_actual():
    assert_equal(unmatched("was 2"), equal_to(1).match(2))
    assert_equal(unmatched("was 'hello'"), equal_to(1).match("hello"))


def test_description_is_repr_of_value():
    assert_equal("'hello'", equal_to("hello").describe())
