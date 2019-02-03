from nose.tools import istest, assert_equal

from precisely.raises import raises
from precisely.results import matched, unmatched


def _function_raises_keyerror(key):
    test_dict = {"in dict": "value"}
    return test_dict[key]


@istest
def matches_when_expected_exception_is_raised():
    matcher = raises(KeyError)
    assert_equal(matched(), matcher.match(lambda: _function_raises_keyerror("not in dict")))


@istest
def matches_when_expected_Exception_exception_is_raised():
    matcher = raises(Exception)

    def _raise_exception():
        raise Exception

    assert_equal(matched(), matcher.match(lambda: _raise_exception()))


@istest
def mismatches_when_no_exception_is_raised():
    matcher = raises(KeyError)
    assert_equal(unmatched("no exception raised"), matcher.match(lambda: _function_raises_keyerror("in dict")))


@istest
def mismatches_when_unexpected_exception_is_raised():
    matcher = raises(ValueError)
    assert_equal(unmatched("raised 'KeyError'"), matcher.match(lambda: _function_raises_keyerror("not in dict")))
