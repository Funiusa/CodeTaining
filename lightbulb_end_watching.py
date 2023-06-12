from datetime import datetime
from typing import List, Optional


def sum_light(
        els: List[datetime],
        start_watching: Optional[datetime] = None,
        end_watching: Optional[datetime] = None
) -> int:
    """
    how long the light bulb has been turned on
    """
    duration = 0
    if start_watching:
        if start_watching == els[-1]:
            return duration
        for date in els[::-1]:
            if start_watching >= date:
                inx = els.index(date)
                if inx % 2 == 0:
                    inx = inx - 1 if inx == len(els) - 1 else inx
                    els[inx] = start_watching
                    els = els[inx:]
                else:
                    els = els[inx + 1:]
                break
        if end_watching:
            els.append(end_watching)
            els.sort()
            index = els.index(end_watching)
            els = els[:index + 1]
        if len(els) % 2 != 0:
            els.append(els[-1])

    for i in range(0, len(els), 2):
        duration += int((els[i + 1] - els[i]).total_seconds())
    return duration


if __name__ == "__main__":
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10)
    ],
        datetime(2015, 1, 12, 10, 30, 0),
        datetime(2015, 1, 12, 11, 0, 0)) == 0
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10)
    ]) == 1220
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10)
    ],
        datetime(2015, 1, 12, 10, 0, 10),
        datetime(2015, 1, 12, 10, 0, 20)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
        datetime(2015, 1, 12, 10, 10, 0),
        datetime(2015, 1, 12, 11, 0, 10)) == 20

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 9, 0),
        datetime(2015, 1, 12, 10, 0, 0)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 9, 0, 0),
        datetime(2015, 1, 12, 10, 5, 0)) == 300
