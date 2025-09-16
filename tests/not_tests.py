from precisely import equal_to, not_
from precisely.results import matched, unmatched
from .testing import assert_equal


def test_matches_when_negated_matcher_does_not_match():
    assert_equal(matched(), not_(equal_to(1)).match(2))


def test_does_not_match_when_negated_matcher_matches():
    assert_equal(unmatched("matched: 1"), not_(equal_to(1)).match(1))


def test_description_includes_description_of_negated_matcher():
    assert_equal("not: 'hello'", not_(equal_to("hello")).describe())
