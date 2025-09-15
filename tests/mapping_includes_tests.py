
from precisely import equal_to, mapping_includes
from precisely.results import matched, unmatched


def test_matches_when_keys_and_values_match():
    matcher = mapping_includes({"a": equal_to(1), "b": equal_to(2)})
    assert matched() == matcher.match({"a": 1, "b": 2})


def test_values_are_coerced_to_matchers():
    matcher = mapping_includes({"a": 1, "b": 2})
    assert matched() == matcher.match({"a": 1, "b": 2})


def test_does_not_match_when_value_does_not_match():
    matcher = mapping_includes({"a": equal_to(1), "b": equal_to(2)})
    assert unmatched("value for key 'b' mismatched:\n * was 3") == matcher.match({"a": 1, "b": 3, "c": 4})


def test_does_not_match_when_keys_are_missing():
    matcher = mapping_includes({"a": equal_to(1), "b": equal_to(2)})
    assert unmatched("was missing key: 'b'") == matcher.match({"a": 1})


def test_matches_when_there_are_extra_keys():
    matcher = mapping_includes({"a": equal_to(1)})
    assert matched() == matcher.match({"a": 1, "b": 1, "c": 1})


def test_description_describes_keys_and_value_matchers():
    matcher = mapping_includes({"a": equal_to(1), "b": equal_to(2)})
    assert "mapping including items:\n * 'a': 1\n * 'b': 2" == matcher.describe()
