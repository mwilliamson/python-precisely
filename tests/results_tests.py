from precisely.results import indented_list


def test_indented_list_indents_children():
    assert indented_list([
        "apple" + indented_list(["banana", "coconut"]),
        "durian",
    ]) == "\n * apple\n    * banana\n    * coconut\n * durian"