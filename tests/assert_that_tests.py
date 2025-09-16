from precisely import assert_that, equal_to
from .testing import assert_equal


def test_assert_that_does_nothing_if_matcher_matches():
    assert_that(1, equal_to(1))


def test_assert_that_raises_assertion_error_if_match_fails():
    try:
        assert_that(1, equal_to(2))
        assert False, "Expected AssertionError"
    except AssertionError as error:
        assert_equal("\nExpected:\n  2\nbut:\n  was 1", str(error))
