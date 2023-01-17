"""
    Stephan has a friend who happens to be a little mechbird.
    Recently, he was trying to teach it how to speak basic language.
    Today the bird spoke its first word: "hieeelalaooo".
    This sounds a lot like "hello", but with too many vowels.
    Stephan asked Nikola for help and he helped to examine how the bird changes words.
    With the information they discovered, we should help them to make a translation module.
The bird converts words by two rules:

    - after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
    - after each vowel letter the bird appends two of the same letter (a ⇒ aaa);

Vowels letters == "aeiouy".

You are given an ornithological phrase as several words which are separated by white-spaces
(each pair of words by one whitespace).
The bird does not know how to punctuate its phrases and only speaks words as letters.
All words are given in lowercase.
You should translate this phrase from the bird language to something more understandable.

Input: A bird phrase as a string.

Output: The translation as a string. 

"""

import re


def translate(bp: str) -> str:
    new = bp
    p1 = sorted(set(re.findall(r"[^\s\daeiouy][aeiouy]", bp)))
    print(p1)
    for m in p1:
        new = new.replace(m, m[0])
    p2 = set(re.findall(r"[aeiouy]{3}", new))
    print(p2)
    for m in p2:
        new = new.replace(m, m[-1])
    return new


if __name__ == "__main__":
    print(bird_language("hieeelalaooo"))
    print(bird_language("hoooowe yyyooouuu duoooiiine"))
    print(bird_language("aaa bo cy da eee fe"))
    print(bird_language("sooooso aaaaaaaaa"))
    print(bird_language("aaabucidyeeefigihoiiijukulemonoooopyqorysotauuuviwuxayyyzu ziyyyxuwivouuutesiriqopaooonimelykijaiiihigefaeeedacybuaaa"))

