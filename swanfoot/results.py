import collections


_Result = collections.namedtuple("_Result", ["is_match", "explanation"])


def matched():
    return _Result(True, None)


def unmatched(explanation):
    return _Result(False, explanation)


def indented_list(items, bullet=None):
    if bullet is None:
        bullet = lambda index: "*"
    return "".join(
        "\n  {0} {1}".format(bullet(index), item.replace("\n", "\n  "))
        for index, item in enumerate(items)
    )


def indexed_indented_list(items):
    return indented_list(items, bullet=lambda index: "{0}:".format(index))
