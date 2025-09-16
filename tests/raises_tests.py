from precisely import is_instance, raises
from precisely.results import matched, unmatched
from .testing import assert_equal


def test_matches_when_expected_exception_is_raised():
    def raise_key_error():
        raise KeyError()

    matcher = raises(is_instance(KeyError))
    assert_equal(matched(), matcher.match(raise_key_error))


def test_mismatches_when_no_exception_is_raised():
    matcher = raises(is_instance(KeyError))
    assert_equal(unmatched("did not raise exception"), matcher.match(lambda: None))


def test_mismatches_when_unexpected_exception_is_raised():
    def raise_key_error():
        raise KeyError()

    matcher = raises(is_instance(ValueError))
    result = matcher.match(raise_key_error)
    assert not result.is_match
    assert _normalise_newlines(result.explanation).startswith(
        "exception did not match: had type KeyError\n\nTraceback (most recent call last):\n",
    )


def test_mismatches_when_value_is_not_callable():
    matcher = raises(is_instance(ValueError))
    assert_equal(unmatched("was not callable"), matcher.match(42))


def test_description_includes_description_of_exception():
    matcher = raises(is_instance(ValueError))
    assert_equal("a callable raising: is instance of ValueError", matcher.describe())


def _normalise_newlines(string):
    return string.replace("\r\n", "\n").replace("\r", "\n")
