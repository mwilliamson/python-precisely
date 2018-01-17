from datetime import datetime, timedelta
from nose.tools import istest, assert_equal

from precisely import close_to
from precisely.results import matched, unmatched


@istest
def close_to_matches_when_actual_is_close_to_value_plus_delta():
    matcher = close_to(42, 1)
    assert_equal(matched(), matcher.match(43))
    assert_equal(matched(), matcher.match(42.5))
    assert_equal(matched(), matcher.match(42))
    assert_equal(matched(), matcher.match(41.5))
    assert_equal(matched(), matcher.match(41))
    assert_equal(unmatched("was 40 (differs from 42 by more than 1)"), matcher.match(40))


@istest
def close_to_matches_datetime_values():
    matcher = close_to(datetime(2018, 1, 17), timedelta(days=1))
    assert_equal(matched(), matcher.match(datetime(2018, 1, 18)))
    assert_equal(matched(), matcher.match(datetime(2018, 1, 17)))
    assert_equal(matched(), matcher.match(datetime(2018, 1, 16)))
    assert_equal(unmatched(
        "was datetime.datetime(2018, 1, 15, 0, 0) (differs from datetime.datetime(2018, 1, 17, 0, 0) by more than datetime.timedelta(1))"
    ),
         matcher.match(datetime(2018, 1, 15))
    )


@istest
def close_to_description_describes_value():
    matcher = close_to(42, 1)
    assert_equal("close to 42 +/- 1", matcher.describe())