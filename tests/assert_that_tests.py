from nose.tools import istest, assert_equal

from spamfoot import assert_that, equal_to


@istest
def assert_that_does_nothing_if_matcher_matches():
    assert_that(1, equal_to(1))


@istest
def assert_that_raises_assertion_error_if_match_fails():
    try:
        assert_that(1, equal_to(2))
        assert False, "Expected AssertionError"
    except AssertionError as error:
        assert_equal("\nExpected: 2\nbut: was 1", str(error))
