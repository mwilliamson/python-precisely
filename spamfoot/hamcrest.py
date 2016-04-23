from . import (
    assert_that,
    all_of,
    anything as _anything,
    equal_to,
    has_property,
    has_properties,
)

def anything():
    return _anything
