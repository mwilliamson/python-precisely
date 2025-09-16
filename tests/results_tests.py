from precisely.results import indented_list
from .testing import assert_equal


def test_indented_list_indents_children():
    assert_equal(
        "\n * apple\n    * banana\n    * coconut\n * durian",
        indented_list([
            "apple" + indented_list(["banana", "coconut"]),
            "durian",
        ])
    )
