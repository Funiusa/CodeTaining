MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code: str) -> str:
    words = code.split("   ")
    line = []
    for word in words:
        decode_value = "".join(MORSE.get(val) for val in word.split(" "))
        line.append(decode_value)
    decode_line = " ".join(line)
    return decode_line.capitalize() if decode_line[0].isalpha() else decode_line


if __name__ == "__main__":
    print("Example:")
    print(morse_decoder("... --- -- .   - . -..- -"))

    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert (
        morse_decoder(
            "..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----"
        )
        == "I was born in 1990"
    )

    print("The mission is done! Click 'Check Solution' to earn rewards!")
