from nose.tools import istest, assert_equal

from precisely import is_instance, raises
from precisely.results import matched, unmatched


def _function_raises_keyerror(key):
    test_dict = {"in dict": "value"}
    return test_dict[key]


@istest
def matches_when_expected_exception_is_raised():
    matcher = raises(is_instance(KeyError))
    assert_equal(matched(), matcher.match(lambda: _function_raises_keyerror("not in dict")))


@istest
def matches_when_expected_Exception_exception_is_raised():
    matcher = raises(is_instance(Exception))

    def _raise_exception():
        raise Exception

    assert_equal(matched(), matcher.match(lambda: _raise_exception()))


@istest
def mismatches_when_no_exception_is_raised():
    matcher = raises(is_instance(KeyError))
    assert_equal(unmatched("did not raise exception"), matcher.match(lambda: None))


@istest
def mismatches_when_unexpected_exception_is_raised():
    matcher = raises(is_instance(ValueError))
    assert_equal(unmatched("exception did not match: had type KeyError"), matcher.match(lambda: _function_raises_keyerror("not in dict")))
