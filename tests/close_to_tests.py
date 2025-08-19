import functools

from nose.tools import assert_equal

from precisely import close_to, is_sequence
from precisely.results import matched, unmatched


def test_close_to_matches_when_actual_is_close_to_value_plus_delta():
    matcher = close_to(42, 1)
    assert_equal(matched(), matcher.match(43))
    assert_equal(matched(), matcher.match(42.5))
    assert_equal(matched(), matcher.match(42))
    assert_equal(matched(), matcher.match(41.5))
    assert_equal(matched(), matcher.match(41))
    assert_equal(unmatched("was 40 (2 away from 42)"), matcher.match(40))


def test_close_to_matches_any_types_supporting_comparison_and_addition_and_subtraction():
    class Instant(object):
        def __init__(self, seconds_since_epoch):
            self.seconds_since_epoch = seconds_since_epoch

        def __sub__(self, other):
            if isinstance(other, Instant):
                return Interval(self.seconds_since_epoch - other.seconds_since_epoch)
            else:
                return NotImplemented

        def __repr__(self):
            return "Instant({})".format(self.seconds_since_epoch)

    @functools.total_ordering
    class Interval(object):
        def __init__(self, seconds):
            self.seconds = seconds

        def __abs__(self):
            return Interval(abs(self.seconds))

        def __eq__(self, other):
            if isinstance(other, Interval):
                return self.seconds == other.seconds
            else:
                return NotImplemented

        def __lt__(self, other):
            if isinstance(other, Interval):
                return self.seconds < other.seconds
            else:
                return NotImplemented

        def __repr__(self):
            return "Interval({})".format(self.seconds)

    matcher = close_to(Instant(42), Interval(1))
    assert_equal(matched(), matcher.match(Instant(43)))
    assert_equal(matched(), matcher.match(Instant(42.5)))
    assert_equal(matched(), matcher.match(Instant(42)))
    assert_equal(matched(), matcher.match(Instant(41.5)))
    assert_equal(matched(), matcher.match(Instant(41)))
    assert_equal(unmatched("was Instant(40) (Interval(2) away from Instant(42))"), matcher.match(Instant(40)))


def test_close_to_description_describes_value():
    matcher = close_to(42, 1)
    assert_equal("close to 42 +/- 1", matcher.describe())


def test_close_to_can_be_used_in_composite_matcher():
    matcher = is_sequence("a", "b", close_to(42, 1))
    assert_equal(matched(), matcher.match(("a", "b", 42)))
