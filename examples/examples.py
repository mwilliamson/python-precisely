import os

from nose.tools import istest

if os.environ.get("HAMCREST"):
    from hamcrest import *
else:
    from spamfoot import *


@istest
def equality():
    assert_that(1, equal_to(2))
