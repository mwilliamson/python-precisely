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

API
---

Use ``assert_that(value, matcher)`` to assert that a value satisfies a matcher.

Many matchers are composed of other matchers.
If they are given a value instead of a matcher,
then that value is wrapped in ``equal_to()``.
For instance, ``has_attrs(name="bob")`` is equivalent to ``has_attrs(name=equal_to("bob"))``.

* ``equal_to(value)``: matches a value if it is equal to ``value`` using ``==``.

* ``has_attrs(**kwargs)``: matches a value if it has the specified attributes.
  For instance:
  
  .. code:: python
  
      assert_that(result, has_attrs(id=is_a(int), name="bob"))

* ``contains_exactly(*args)``: matches an iterable if it has the same elements in any order.
  For instance:
  
  .. code:: python
  
      assert_that(result, contains_exactly("a", "b"))
      # Matches ["a", "b"] and ["b", "a"],
      # but not ["a", "a", "b"] nor ["a"] nor ["a", "b", "c"]

* ``is_same_sequence(*args)``: matches an iterable if it has the same elements in the same order.
  For instance:
  
  .. code:: python
  
      assert_that(result, is_same_sequence("a", "b"))
      # Matches ["a", "b"] but not ["b", "a"]

* ``anything``: matches all values.

* ``instance_of(type)``: matches any value where ``isinstance(value, type))``.

* ``all_of(*matchers)``: matchers a value if all sub-matchers match.
  For instance:
  
  .. code:: python
  
      assert_that(result, all_of(
          is_instance(User),
          has_attrs(name="bob"),
      ))

* ``all_of(*matchers)``: matchers a value if any sub-matcher matches.
  For instance:
  
  .. code:: python
  
      assert_that(result, any_of(
          equal_to("x=1, y=2"),
          equal_to("y=2, x=1"),
      ))

* ``has_feature(name, extract, matcher)``: matches ``value`` if ``extract(value)`` matches ``matcher``.
  For instance:
  
  .. code:: python
  
      assert_that(result, has_feature("len", len, equal_to(2)))
  
  For clarity, it often helps to extract the use of ``has_feature`` into its own function:
  
  .. code:: python
  
      def has_len(matcher):
          return has_feature("len", len, matcher)
      
      assert_that(result, has_len(equal_to(2)))

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
