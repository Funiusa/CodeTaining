from typing import Iterable


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
