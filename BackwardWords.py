""" Требуется обратить порядок букв в каждом слове предоставленной строки,
    так чтобы слова остались на своих местах. """


def backward_words(source: str) -> str:
    text = ""
    idx1 = 0
    for word in source.split():
        idx2 = source.find(word, idx1)
        text += source[idx1:idx2] + word[::-1]
        idx1 = idx2 + len(word)
    return text + source[idx1:-1]
