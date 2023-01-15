def time_converter(time: str) -> str:
    t = time.split(':')
    hour, minute = int(t[0]), t[1]
    if hour >= 12:
        return f"{hour - 12 if hour != 12 else '12'}:{minute} p.m."
    return f"{hour if hour > 0 else '12'}:{minute} a.m."


if __name__ == "__main__":
    print(time_converter("12:30"))
    print(time_converter("09:00"))
    print(time_converter("02:45"))
    print(time_converter("22:54"))
    print(time_converter("17:12"))
    print(time_converter("00:01"))
    print(time_converter("13:10"))
    print(time_converter("23:59"))
    print(time_converter("00:00"))
