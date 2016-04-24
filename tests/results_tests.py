from nose.tools import istest, assert_equal

from swanfoot.results import indented_list  


@istest
def indented_list_indents_children():
    assert_equal(
        "\n  * apple\n    * banana\n    * coconut\n  * durian",
        indented_list([
            "apple" + indented_list(["banana", "coconut"]),
            "durian",
        ])
    )
