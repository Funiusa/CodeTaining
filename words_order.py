def words_order(sentence: str, words: list) -> bool:
    sentence_list = []
    for word in sentence.split():
        if word in words and word not in sentence_list:
            sentence_list.append(word)
            if words == sentence_list:
                break
    return sentence_list == words


if __name__ == "__main__":
    assert words_order("hi world im here", ["world", "here"]) == True
    assert words_order("hi world im here", ["here", "world"]) == False
    assert words_order("hi world im here", ["world"]) == True
    assert words_order("hi world im here", ["world", "here", "hi"]) == False
    assert words_order("hi world im here", ["world", "im", "here"]) == True
    assert words_order("hi world im here", ["world", "hi", "here"]) == False
    assert words_order("hi world im here World", ["world", "World"]) == True
    assert words_order("hi world im here", ["world", "World"]) == False
    assert words_order("hi world im here", ["country", "world"]) == False
    assert words_order("hi world im here", ["wo", "rld"]) == False
    assert words_order("", ["world", "here"]) == False
    assert words_order("hi world world im here", ["world", "world"]) == False
    assert (
        words_order("hi world world im here hi world world im here", ["world", "here"])
        == True
    )
