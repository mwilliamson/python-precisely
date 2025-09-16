from precisely import anything
from precisely.results import matched
from .testing import assert_equal


def test_matches_anything():
    assert_equal(matched(), anything.match(4))
    assert_equal(matched(), anything.match(None))
    assert_equal(matched(), anything.match("Hello"))


def test_description_is_anything():
    assert_equal("anything", anything.describe())

