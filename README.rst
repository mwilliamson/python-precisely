Precisely: matcher library for Python
====================================

Installation
------------

::

    pip install precisely

Alternatives
------------

PyHamcrest is another Python implemention of matchers. I prefer the error
messages that this project produces, but feel free to judge for yourself:

.. code:: python

    # Precisely
    from precisely import assert_that, is_same_sequence, has_attrs

    assert_that(
        [
            User("bob", "jim@example.com"),
            User("jim", "bob@example.com"),
        ],
        is_same_sequence(
            has_attrs(username="bob", email_address="bob@example.com"),
            has_attrs(username="jim", email_address="jim@example.com"),
        )
    )

    # Expected: iterable containing in order:
    #   0: attributes:
    #     * username: 'bob'
    #     * email_address: 'bob@example.com'
    #   1: attributes:
    #     * username: 'jim'
    #     * email_address: 'jim@example.com'
    # but: element at index 0 mismatched:
    #   * attribute email_address: was 'jim@example.com'

    # Hamcrest
    from hamcrest import assert_that, contains, has_properties

    assert_that(
        [
            User("bob", "jim@example.com"),
            User("jim", "bob@example.com"),
        ],
        contains(
            has_properties(username="bob", email_address="bob@example.com"),
            has_properties(username="jim", email_address="jim@example.com"),
        )
    )

    # Hamcrest error:
    # Expected: a sequence containing [(an object with a property 'username' matching 'bob' and an object with a property 'email_address' matching 'bob@example.com'), (an object with a property 'username' matching 'jim' and an object with a property 'email_address' matching 'jim@example.com')]
    #      but: item 0: an object with a property 'email_address' matching 'bob@example.com' property 'email_address' was 'jim@example.com'
