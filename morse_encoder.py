MORSE = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": " ",
}


def morse_encoder(text: str) -> str:
    return " ".join((MORSE.get(elem.lower()) for elem in text))


if __name__ == "__main__":
    print("Example:")
    # print(morse_encoder("some text"))

    # assert morse_encoder("some text") == "... --- -- .   - . -..- -"
    assert (
        morse_encoder("I was born in 1990")
        == "..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----"
    )

    print("The mission is done! Click 'Check Solution' to earn rewards!")
