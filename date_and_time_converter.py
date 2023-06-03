def date_time(time: str) -> str:
    from datetime import datetime

    dt = datetime.strptime(time, "%d.%m.%Y %H:%M")
    minute = "minute" if dt.minute == 1 else "minutes"
    hour = "hour" if dt.hour == 1 else "hours"
    month = dt.strftime("%B")
    return f"{dt.day} {month} {dt.year} year {dt.hour} {hour} {dt.minute} {minute}"


if __name__ == "__main__":
    print("Example:")

    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    assert date_time("09.05.1945 06:07") == "9 May 1945 year 6 hours 7 minutes"

    print("The mission is done! Click 'Check Solution' to earn rewards!")
