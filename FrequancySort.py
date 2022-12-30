from typing import Iterable

""" Sort the given list so that its elements end up in the decreasing frequency order,
    that is, the number of times they appear in elements. 
    If two elements have the same frequency, 
    they should end up in the same order as the first appearance in the list.

    If you want to practice more with the similar case, try Frequency Sorting mission.

    Input: List

    Output: List or another Iterable (tuple, iterator, generator) 
"""


def frequency_sort(source: list) -> Iterable[str | int]:
    tmp_dict = {}
    for elem in set(source):
        if source.count(elem) in tmp_dict.keys():
            tmp_dict[source.count(elem)] += ((source.index(elem), elem),)
            tmp_dict[source.count(elem)] = sorted(tmp_dict[source.count(elem)], key=lambda x: x[0])
        else:
            tmp_dict.update({source.count(elem): ((source.index(elem), elem),)})
    od = sorted(tmp_dict.items(), reverse=True)
    ret = []
    for k, values in od:
        for val in values:
            ret += [val[1]] * k
    return ret
