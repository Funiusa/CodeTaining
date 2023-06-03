def sort_by_ext(files: list[str]) -> list[str]:
    result, extensions = [], []
    for file in files:
        chunk = file.split(".")
        if chunk[-2] and chunk[-1]:
            extensions.append(file)
        else:
            result.append(file)

    result.sort()
    extensions.sort()
    extensions.sort(key=lambda x: x.split(".")[-1])
    result.extend(extensions)
    return result


if __name__ == "__main__":
    print("Example:")
    assert sort_by_ext(["1.cad", "2.bat", "1.aa", "1.bat"]) == [
        "1.aa",
        "1.bat",
        "2.bat",
        "1.cad",
    ]
    assert sort_by_ext(
        [
            ".config",
            "my.doc",
            "1.exe",
            "345.bin",
            "green.bat",
            "format.c",
            "no.name.",
            "best.test.exe",
        ]
    ) == [
        ".config",
        "no.name.",
        "green.bat",
        "345.bin",
        "format.c",
        "my.doc",
        "1.exe",
        "best.test.exe",
    ]
    assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"]
    assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
        "1.aa",
        "1.bat",
        "2.bat",
        "1.cad",
    ]
    assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]) == [
        ".bat",
        "1.aa",
        "1.bat",
        "1.cad",
    ]
    assert sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]) == [
        ".aa",
        ".bat",
        "1.bat",
        "1.cad",
    ]
    assert sort_by_ext(["1.cad", "1.", "1.aa"]) == ["1.", "1.aa", "1.cad"]
    assert sort_by_ext(["1.cad", "1.bat", "1.aa", "1.aa.doc"]) == [
        "1.aa",
        "1.bat",
        "1.cad",
        "1.aa.doc",
    ]
    assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".aa.doc"]) == [
        "1.aa",
        "1.bat",
        "1.cad",
        ".aa.doc",
    ]
