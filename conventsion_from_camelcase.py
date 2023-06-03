def from_camel_case(name: str) -> str:
    import re

    split_name = re.findall("[A-Z][a-z]+|[A-Z]", name)
    return "_".join(word.lower() for word in split_name)


if __name__ == "__main__":
    print("Example:")
    print(from_camel_case("MyFunctionName"))

    # These "asserts" are used for self-checking
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"

    print("The mission is done! Click 'Check Solution' to earn rewards!")
