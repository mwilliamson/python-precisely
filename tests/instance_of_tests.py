from nose.tools import istest, assert_equal

from precisely import instance_of
from precisely.results import matched, unmatched


@istest
def matches_when_value_is_instance_of_class():
    assert_equal(matched(), instance_of(int).match(1))


@istest
def explanation_of_mismatch_contains_actual_type():
    assert_equal(unmatched("had type float"), instance_of(int).match(1.0))


@istest
def description_includes_expected_type():
    assert_equal("instance of int", instance_of(int).describe())
