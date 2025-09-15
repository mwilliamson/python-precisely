
from precisely import equal_to
from precisely.results import matched, unmatched


def test_matches_when_values_are_equal():
    assert matched() == equal_to(1).match(1)


def test_explanation_of_mismatch_contains_repr_of_actual():
    assert unmatched("was 2") == equal_to(1).match(2)
    assert unmatched("was 'hello'") == equal_to(1).match("hello")


def test_description_is_repr_of_value():
    assert equal_to("hello").describe() == "'hello'"
