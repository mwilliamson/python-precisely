import os
import collections

from nose.tools import istest

if os.environ.get("HAMCREST"):
    from hamcrest import *
else:
    from spamfoot import *


User = collections.namedtuple("User", ["username", "email_address"]) 


@istest
def test_equal_to():
    assert_that(1, equal_to(2))


@istest
def test_has_property_wrong_value():
    assert_that(User("bob", None), has_property("username", "bobbity"))


@istest
def test_has_property_missing():
    assert_that("bob", has_property("username", "bobbity"))
