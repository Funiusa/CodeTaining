from typing import Union


def sun_angle(time: str) -> Union[float, str]:
    time_parts = time.split(":")
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    total_minutes = hours * 60 + minutes
    degree = total_minutes / 4 - 90

    if 0 <= degree <= 180:
        return degree
    return "I don't see the sun!"


if __name__ == "__main__":
    print("Example:")
    print(sun_angle("00:00"))
    print(sun_angle("07:00"))

    assert sun_angle("07:00") == 15
    assert sun_angle("12:15") == 93.75

    print("The mission is done! Click 'Check Solution' to earn rewards!")
