Precisely: better assertions for Python tests
=============================================

Precisely allows you to write precise assertions so you only test the behaviour you're really interested in.
This makes it clearer to the reader what the expected behaviour is,
and makes tests less brittle.
This also allows better error messages to be generated when assertions fail.
Inspired by Hamcrest_.

.. _Hamcrest: http://hamcrest.org

For instance, suppose we want to make sure that a ``unique`` function removes duplicates from a list.
We might write a test like so:

.. code:: python

    from precisely import assert_that, contains_exactly
    
    def test_unique_removes_duplicates():
        result = unique(["a", "a", "b", "a", "b"])
        assert_that(result, contains_exactly("a", "b"))

The assertion will pass so long as ``result`` contains ``"a"`` and ``"b"`` in any order,
but no other items.
Unlike, say, ``assert result == ["a", "b"]``, our assertion ignores the ordering of elements.
This is useful when:

* the ordering of the result is non-determistic, such as when using ``set``.

* the ordering isn't specified in the contract of ``unique``.
  If we assert a particular ordering, then we'd be testing the implementation rather than the contract.

* the ordering is specified in the contract of ``unique``,
  but the ordering is tested in a separate test case.

When the assertion fails,
rather than just stating the two values weren't equal,
the error message will describe the failure in more detail.
For instance, if unique has the value ``["a", "a", "b"]``,
we'd get the failure message::

    Expected: iterable containing in any order:
      * 'a'
      * 'b'
    but: had extra elements:
      * 'a'

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
