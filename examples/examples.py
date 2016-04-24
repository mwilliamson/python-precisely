import os
import collections

from nose.tools import istest

if os.environ.get("HAMCREST"):
    from hamcrest import *
else:
    from swanfoot.hamcrest import *


User = collections.namedtuple("User", ["username", "email_address"]) 


@istest
def test_anything():
    assert_that(1, anything())

@istest
def test_equal_to():
    assert_that(1, equal_to(2))


@istest
def test_has_property_wrong_value():
    assert_that(User("bob", None), has_property("username", "bobbity"))


@istest
def test_has_property_missing():
    assert_that("bob", has_property("username", "bobbity"))


@istest
def test_has_properties_wrong_value():
    assert_that(User("bob", "bob@example.com"), has_properties(
        username="bob",
        email_address="bobbity@example.com",
    ))


@istest
def test_all_of():
    assert_that(User("bob", "bob@example.com"), all_of(
        has_property("username", "bob"),
        has_property("email_address", "bobbity@example.com"),
    ))


@istest
def test_contains_inanyorder_missing_elements():
    assert_that(
        [
            User("bob", "jim@example.com"),
            User("jim", "bob@example.com"),
        ],
        contains_inanyorder(
            has_properties(username="bob", email_address="bob@example.com"),
            has_properties(username="jim", email_address="jim@example.com"),
        )
    )


@istest
def test_contains_inanyorder_extra_elements():
    assert_that(
        ["apple", "banana"],
        contains_inanyorder("apple"),
    )
