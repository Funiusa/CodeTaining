"""
    You prefer a good old 12-hour time format.
    But the modern world we live in would rather use the 24-hour format and you see it everywhere.
    Your task is to convert the time from the 24-h format into 12-h format by following the next rules:

    - the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday);
    - if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'.

    Input: Time in the 24-hour format (as a string).

    Output: Time in the 12-hour format (as a string).
"""


def time_converter(time: str) -> str:
    t = time.split(":")
    hour, minute = int(t[0]), t[1]
    if hour >= 12:
        return f"{hour - 12 if hour != 12 else '12'}:{minute} p.m."
    return f"{hour if hour > 0 else '12'}:{minute} a.m."
