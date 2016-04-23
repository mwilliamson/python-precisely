import collections


_Result = collections.namedtuple("_Result", ["is_match", "explanation"])


def matched():
    return _Result(True, None)


def unmatched(explanation):
    return _Result(False, explanation)
