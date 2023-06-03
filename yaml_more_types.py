def convert_value(value, target_type):
    try:
        return target_type(value)
    except (ValueError, TypeError):
        # Handle conversion errors
        return None


def yaml(a: str) -> dict:
    import re

    result = {}
    elements = re.findall(r"(\w+):\s*([\S ]*)", a)
    for key, val in elements:
        try:
            result[key] = int(val)
        except ValueError:
            val = val.strip()
            if val.lower() == "false":
                val = False
            elif val.lower() == "true":
                val = True
            elif val in "null" or not val:
                val = None
            elif val.startswith('"') and val.endswith('"'):
                val = val.replace("\\", "")
                val = val[1:-1]
            result[key] = val
    return result


if __name__ == "__main__":
    assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
    assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
        "age": 12,
        "name": "Alex Fox",
        "class": "12b",
    }
    assert yaml('name: "Alex Fox"\nage: 12\n\nclass: 12b') == {
        "age": 12,
        "name": "Alex Fox",
        "class": "12b",
    }
    assert yaml('name: "Alex \\"Fox\\""\nage: 12\n\nclass: 12b') == {
        "age": 12,
        "name": 'Alex "Fox"',
        "class": "12b",
    }
    assert yaml('name: "Bob Dylan"\nchildren: 6\nalive: false') == {
        "name": "Bob Dylan",
        "alive": False,
        "children": 6,
    }
    assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding:') == {
        "coding": None,
        "name": "Bob Dylan",
        "children": 6,
    }
    assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding: null') == {
        "coding": None,
        "name": "Bob Dylan",
        "children": 6,
    }
    assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding: "null" ') == {
        "coding": "null",
        "name": "Bob Dylan",
        "children": 6,
    }

    print("The mission is done! Click 'Check Solution' to earn rewards!")
