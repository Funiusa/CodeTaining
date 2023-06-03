def yaml(a: str) -> dict:
    import re

    result = {}
    elements = re.findall(r"(\w+):\s*([\S ]+)", a)
    for key, val in elements:
        try:
            result[key] = int(val)
        except ValueError:
            result[key] = val
    return result


if __name__ == "__main__":
    print("Example:")
    print(
        yaml(
            """name: Alex
    age: 12"""
        )
    )

    # These "asserts" are used for self-checking
    assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
    assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
        "age": 12,
        "name": "Alex Fox",
        "class": "12b",
    }

    print("The mission is done! Click 'Check Solution' to earn rewards!")
