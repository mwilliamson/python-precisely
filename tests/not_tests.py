from nose.tools import istest, assert_equal

from precisely import equal_to, not_
from precisely.results import matched, unmatched


@istest
def matches_when_negated_matcher_does_not_match():
    assert_equal(matched(), not_(equal_to(1)).match(2))


@istest
def does_not_match_when_negated_matcher_matches():
    assert_equal(unmatched("matched: 1"), not_(equal_to(1)).match(1))


@istest
def description_includes_description_of_negated_matcher():
    assert_equal("not: 'hello'", not_(equal_to("hello")).describe())
