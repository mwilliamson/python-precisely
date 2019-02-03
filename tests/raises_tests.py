from nose.tools import istest, assert_equal

from precisely import is_instance, raises
from precisely.results import matched, unmatched


@istest
def matches_when_expected_exception_is_raised():
    def raise_key_error():
        raise KeyError()

    matcher = raises(is_instance(KeyError))
    assert_equal(matched(), matcher.match(raise_key_error))


@istest
def mismatches_when_no_exception_is_raised():
    matcher = raises(is_instance(KeyError))
    assert_equal(unmatched("did not raise exception"), matcher.match(lambda: None))


@istest
def mismatches_when_unexpected_exception_is_raised():
    def raise_key_error():
        raise KeyError()

    matcher = raises(is_instance(ValueError))
    assert_equal(unmatched("exception did not match: had type KeyError"), matcher.match(raise_key_error))


@istest
def mismatches_when_value_is_not_callable():
    matcher = raises(is_instance(ValueError))
    assert_equal(unmatched("was not callable"), matcher.match(42))


@istest
def description_includes_description_of_exception():
    matcher = raises(is_instance(ValueError))
    assert_equal("a callable raising: is instance of ValueError", matcher.describe())
