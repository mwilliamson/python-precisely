from precisely import is_instance
from precisely.results import matched, unmatched
from .testing import assert_equal


def test_matches_when_value_is_instance_of_class():
    assert_equal(matched(), is_instance(int).match(1))


def test_explanation_of_mismatch_contains_actual_type():
    assert_equal(unmatched("had type float"), is_instance(int).match(1.0))


def test_description_includes_expected_type():
    assert_equal("is instance of int", is_instance(int).describe())
