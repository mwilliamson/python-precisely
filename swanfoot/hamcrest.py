from . import (
    assert_that,
    all_of,
    anything as _anything,
    contains_exactly as contains_inanyorder,
    equal_to,
    has_property,
    has_properties,
)

def anything():
    return _anything
