
from precisely import anything
from precisely.results import matched


def test_matches_anything():
    assert matched() == anything.match(4)
    assert matched() == anything.match(None)
    assert matched() == anything.match("Hello")


def test_description_is_anything():
    assert "anything" == anything.describe()

