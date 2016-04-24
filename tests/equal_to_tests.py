from nose.tools import istest, assert_equal

from swanfoot import equal_to
from swanfoot.results import matched, unmatched


@istest
def matches_when_values_are_equal():
    assert_equal(matched(), equal_to(1).match(1))


@istest
def explanation_of_mismatch_contains_repr_of_actual():
    assert_equal(unmatched("was 2"), equal_to(1).match(2))
    assert_equal(unmatched("was 'hello'"), equal_to(1).match("hello"))


@istest
def description_is_repr_of_value():
    assert_equal("'hello'", equal_to("hello").describe())
