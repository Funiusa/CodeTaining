""" TESTS for all """
from FirstWord import first_word
from RightToLeft import left_join
from DaysBetween import days_diff
from BackwardWords import backward_words
from BiggerPrice import bigger_price
from PopularWords import popular_words
from SecondIndex import second_index
from FrequancySort import frequency_sort
from MissingNumber import missing_number
from AbsoluteSorted import checkio
from GoesRightAfter import goes_after
from TimeConverter import time_converter
from SumByType import sum_by_types
from BirdLanguage import translate
from CommonWords import common_words
from followInstructions import follow
from Pangram import check_pangram
from MostWantedLetter import most_wanted_letters
from LetterQueue import letter_queue


def test_right_to_left():
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
    assert left_join(("brightness wright",)) == "bleftness wleft"
    assert left_join(("enough", "jokes")) == "enough,jokes"
    assert left_join(("r", "i", "g", "h", "t")) == "r,i,g,h,t"
    assert (
        left_join(
            (
                "lorem",
                "ipsum",
                "dolor",
                "sit",
                "amet",
                "consectetuer",
                "adipiscing",
                "elit",
                "aenean",
                "commodo",
                "ligula",
                "eget",
                "dolor",
                "aenean",
                "massa",
                "cum",
                "sociis",
                "natoque",
                "penatibus",
                "et",
                "magnis",
                "dis",
                "parturient",
                "montes",
                "nascetur",
                "ridiculus",
                "mus",
                "donec",
                "quam",
                "felis",
                "ultricies",
                "nec",
                "pellentesque",
                "eu",
                "pretium",
                "quis",
                "sem",
                "nulla",
                "consequat",
                "massa",
                "quis",
            )
        )
        == "lorem,ipsum,dolor,sit,amet,consectetuer,adipiscing,elit,aenean,commodo,ligula,eget,dolor,aenean,massa,cum,sociis,natoque,penatibus,et,magnis,dis,parturient,montes,nascetur,ridiculus,mus,donec,quam,felis,ultricies,nec,pellentesque,eu,pretium,quis,sem,nulla,consequat,massa,quis"
    )

    assert (
        left_join(
            (
                "right",
                "right",
                "right",
                "right",
                "right",
                "right",
                "right",
                "right",
                "right",
                "right",
                "right",
                "right",
                "right",
                "right",
                "right",
                "right",
                "right",
                "right",
                "right",
                "right",
            )
        )
        == "left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left"
    )

    assert (
        left_join(
            (
                "right",
                "left",
                "right",
                "left",
                "right",
                "left",
                "right",
                "left",
                "right",
                "left",
                "right",
                "left",
                "right",
                "left",
                "right",
                "left",
                "right",
                "left",
                "right",
                "left",
            )
        )
        == "left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left"
    )


def test_first_word():
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word(",greetings, friends") == "greetings"
    assert first_word(", greetings , friends") == "greetings"
    assert first_word(",greetings , friends") == "greetings"

    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Holy Edison") == "Holy"
    assert first_word("Don't speak... I know just what you're saying") == "Don't"

    assert first_word(".") == ""
    assert first_word(". ") == ""
    assert first_word(" ") == ""
    assert first_word("") == ""


def test_days_days_diff():
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    assert days_diff((14, 1, 27), (14, 1, 1)) == 26
    assert days_diff((1992, 10, 28), (1989, 6, 23)) == 1223
    assert days_diff((1622, 10, 4), (3555, 10, 12)) == 706021
    assert days_diff((5871, 8, 23), (6155, 6, 14)) == 103659
    assert days_diff((4632, 11, 18), (8077, 10, 26)) == 1258238
    assert days_diff((696, 5, 7), (9241, 6, 27)) == 3121048
    assert days_diff((6051, 1, 23), (4129, 8, 9))


def test_backward_words():
    assert backward_words("") == ""
    assert backward_words("world") == "dlrow"
    assert backward_words("hello world") == "olleh dlrow"
    assert backward_words("hello   world") == "olleh   dlrow"
    assert backward_words("welcome to a game") == "emoclew ot a emag"
    assert (backward_words(f"[{'  uhi  '}]")) == "[  ihu  ]"
    assert (backward_words("Hello[ ]world")) == "[olleH dlrow]"
    assert (backward_words("olleH[   ]dlrow")) == "[Hello   world]"
    assert (backward_words("[  HooH eldoodle ]")) == "[  HooH eldoodle ]"
    assert (
        backward_words("nehW[ era uoy     og ot ]?peels")
    ) == "[When are you     go to sleep?]"
    assert (backward_words("welcome[ to the ]game")) == "[emoclew ot eht emag]"
    assert (backward_words("sineD___olleH")) == "Hello___Denis"
    assert (
        backward_words(f"[{'   ecaps  erom    secaps '}]")
    ) == "[   space  more    spaces ]"
    assert (
        backward_words("  woh tuoba le odle   odarodle ?")
    ) == "  how about el eldo   eldorado ?"
    assert (backward_words("Hello olleH")) == "olleH Hello"
    assert backward_words("ha ha ha this is cool") == "ah ah ah siht si looc"


def test_bigger_price():
    assert bigger_price(
        2,
        [
            {"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 15},
            {"name": "water", "price": 1},
        ],
    ) == [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]

    assert bigger_price(
        1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}]
    ) == [{"name": "whiteboard", "price": 170}]

    assert bigger_price(
        3,
        [
            {"name": "bread", "price": 10},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 100},
            {"name": "water", "price": 1},
        ],
    ) == [
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 100},
        {"name": "bread", "price": 10},
    ]

    assert bigger_price(
        2,
        [
            {"name": "bread", "price": 1200},
            {"name": "wine", "price": 13},
            {"name": "meat", "price": 300},
            {"name": "water", "price": 1},
        ],
    ) == [{"name": "bread", "price": 1200}, {"name": "meat", "price": 300}]


def test_popular_words():
    assert popular_words(
        "\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n",
        ["i", "was", "three", "near"],
    ) == {"i": 4, "was": 3, "three": 0, "near": 0}

    assert popular_words(
        "\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n",
        ["one", "two", "three"],
    ) == {"one": 1, "two": 1, "three": 0}

    assert popular_words(
        "It's flying from somewhere\nAs fast as it can\nI couldn't keep up with it\nNot if I ran",
        ["it's", "ran", "i"],
    ) == {"it's": 1, "ran": 1, "i": 2}

    assert popular_words(
        "And the Raven never flitting still is sitting still is sitting\n"
        "On the pallid bust of Pallas just above my chamber door\n"
        "And his eyes have all the seeming of a demon’s that is dreaming\n"
        "And the lamp-light o’er him streaming throws his shadow on the floor\n"
        "And my soul from out that shadow that lies floating on the floor\n"
        "Shall be lifted nevermore",
        ["raven", "still", "is", "floor", "nevermore"],
    ) == {"raven": 1, "still": 2, "is": 3, "floor": 2, "nevermore": 1}

    assert popular_words(
        "I will go to the cinema\nNo you will not", ["i", "will", "no"]
    ) == {"i": 1, "will": 2, "no": 1}


def test_second_index():
    assert second_index("sims", "s") == 3
    assert second_index("find the river", "e") == 12
    assert second_index("hi", " ") is None
    assert second_index("hi mayor", " ") is None
    assert second_index("denis what do you did", "d") == 11
    assert second_index("some text", "") == 1  # ?
    assert second_index("hi", " ") is None
    assert second_index("hi mayor", " ") is None
    assert second_index("hi mr Mayor", " ") == 5
    assert second_index("hi", "i") is None
    assert second_index("abc", "d") is None
    assert second_index("see you", "e") == 2
    assert second_index("three occurrences", "r") == 10


def test_frequency_sort():
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [
        4,
        4,
        4,
        4,
        2,
        2,
        2,
        6,
        6,
    ]
    assert list(frequency_sort(["bob", "bob", "carl", "alex", "bob"])) == [
        "bob",
        "bob",
        "bob",
        "carl",
        "alex",
    ]
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    assert list(frequency_sort([6, 3])) == [6, 3]
    assert list(frequency_sort([1, 1, 1, 1])) == [1, 1, 1, 1]
    assert list(frequency_sort([1, 2, 2, 1])) == [1, 1, 2, 2]


def test_missing_number():
    assert missing_number([1, 4, 2, 5]) == 3
    assert missing_number([2, 6, 8]) == 4
    assert missing_number([10, 15, 20, 30]) == 25
    assert missing_number([2, 5]) == 0
    assert missing_number([1, 4, 3, 2, 5, 9, 6, 10, 8, 5]) == 7
    assert missing_number([105, 5, 45, 25, 65]) == 85
    assert missing_number([5, 25, 30, 20, 15]) == 10
    assert missing_number([0, 1, 3, 4, 2, 6, 9, 7, 8]) == 5


def test_checkio():
    assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
    assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
    assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
    assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
    assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
    assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
    assert checkio([0]) == [0]
    assert checkio(
        [
            -99,
            -98,
            -97,
            -96,
            -95,
            -94,
            -93,
            -92,
            -91,
            -90,
            -89,
            -88,
            -87,
            -86,
            -85,
            -84,
            -83,
            -82,
            -81,
            -80,
            -79,
            -78,
            -77,
            -76,
            -75,
            -74,
            -73,
            -72,
            -71,
            -70,
            -69,
            -68,
            -67,
            -66,
            -65,
            -64,
            -63,
            -62,
            -61,
            -60,
            -59,
            -58,
            -57,
            -56,
            -55,
            -54,
            -53,
            -52,
            -51,
            -50,
            -49,
            -48,
            -47,
            -46,
            -45,
            -44,
            -43,
            -42,
            -41,
            -40,
            -39,
            -38,
            -37,
            -36,
            -35,
            -34,
            -33,
            -32,
            -31,
            -30,
            -29,
            -28,
            -27,
            -26,
            -25,
            -24,
            -23,
            -22,
            -21,
            -20,
            -19,
            -18,
            -17,
            -16,
            -15,
            -14,
            -13,
            -12,
            -11,
            -10,
            -9,
            -8,
            -7,
            -6,
            -5,
            -4,
            -3,
            -2,
            -1,
            0,
        ]
    ) == [
        0,
        -1,
        -2,
        -3,
        -4,
        -5,
        -6,
        -7,
        -8,
        -9,
        -10,
        -11,
        -12,
        -13,
        -14,
        -15,
        -16,
        -17,
        -18,
        -19,
        -20,
        -21,
        -22,
        -23,
        -24,
        -25,
        -26,
        -27,
        -28,
        -29,
        -30,
        -31,
        -32,
        -33,
        -34,
        -35,
        -36,
        -37,
        -38,
        -39,
        -40,
        -41,
        -42,
        -43,
        -44,
        -45,
        -46,
        -47,
        -48,
        -49,
        -50,
        -51,
        -52,
        -53,
        -54,
        -55,
        -56,
        -57,
        -58,
        -59,
        -60,
        -61,
        -62,
        -63,
        -64,
        -65,
        -66,
        -67,
        -68,
        -69,
        -70,
        -71,
        -72,
        -73,
        -74,
        -75,
        -76,
        -77,
        -78,
        -79,
        -80,
        -81,
        -82,
        -83,
        -84,
        -85,
        -86,
        -87,
        -88,
        -89,
        -90,
        -91,
        -92,
        -93,
        -94,
        -95,
        -96,
        -97,
        -98,
        -99,
    ]
    assert checkio([-2, 1]) == [1, -2]
    assert checkio([0, 1]) == [0, 1]
    assert checkio([3, -76]) == [3, -76]
    assert checkio(
        [
            40,
            11,
            28,
            99,
            72,
            -23,
            88,
            15,
            47,
            68,
            56,
            93,
            60,
            -59,
            -18,
            -37,
            27,
            -46,
            53,
            30,
        ]
    ) == [
        11,
        15,
        -18,
        -23,
        27,
        28,
        30,
        -37,
        40,
        -46,
        47,
        53,
        56,
        -59,
        60,
        68,
        72,
        88,
        93,
        99,
    ]
    assert checkio([7]) == [7]
    assert checkio([-68, 57, -58, 55, -99, 10, 14]) == [10, 14, 55, 57, -58, -68, -99]
    assert checkio([69, -40, 22, 79, 2, -26, -58, -96, 73, -46, -15, -59, 47]) == [
        2,
        -15,
        22,
        -26,
        -40,
        -46,
        47,
        -58,
        -59,
        69,
        73,
        79,
        -96,
    ]
    assert checkio([35, -24, 83]) == [-24, 35, 83]
    assert checkio(
        [
            32,
            -54,
            50,
            -78,
            9,
            -31,
            -11,
            -89,
            16,
            -85,
            -79,
            -13,
            -68,
            -30,
            -53,
            22,
            -25,
            59,
            24,
        ]
    ) == [
        9,
        -11,
        -13,
        16,
        22,
        24,
        -25,
        -30,
        -31,
        32,
        50,
        -53,
        -54,
        59,
        -68,
        -78,
        -79,
        -85,
        -89,
    ]
    assert checkio([25, -69]) == [25, -69]
    assert checkio([66]) == [66]
    assert checkio([-97, 57, 52, 96]) == [52, 57, 96, -97]
    assert checkio([-41, 71, -99, 20, 2, 43, 64, 33, 23, 45, 16]) == [
        2,
        16,
        20,
        23,
        33,
        -41,
        43,
        45,
        64,
        71,
        -99,
    ]

    assert checkio(
        [96, 7, -66, -25, 16, -8, -68, -41, 98, -99, 58, 88, 67, -45, 89, 31]
    ) == [7, -8, 16, -25, 31, -41, -45, 58, -66, 67, -68, 88, 89, 96, 98, -99]
    assert checkio([62, 49, 13, 99, -75, 15, -74, -40, -72, -88, -66, 26, -71, 48]) == [
        13,
        15,
        26,
        -40,
        48,
        49,
        62,
        -66,
        -71,
        -72,
        -74,
        -75,
        -88,
        99,
    ]
    assert checkio([2, -36, 42, -45, -67, 7, 86]) == [2, 7, -36, 42, -45, -67, 86]
    assert checkio([-70, -78, 42, -31, -28, 80, 5, 53, 90, -50, 86, 33, 60, 54]) == [
        5,
        -28,
        -31,
        33,
        42,
        -50,
        53,
        54,
        60,
        -70,
        -78,
        80,
        86,
        90,
    ]
    assert checkio([32, 23, 45, 78]) == [23, 32, 45, 78]
    assert checkio([46, -83, 43, 28, -96, -84, -4, -21, 50, -65, -47]) == [
        -4,
        -21,
        28,
        43,
        46,
        -47,
        50,
        -65,
        -83,
        -84,
        -96,
    ]
    assert checkio([56, -71, -46, 25, -45, 5, -72, 58, 48, 2]) == [
        2,
        5,
        25,
        -45,
        -46,
        48,
        56,
        58,
        -71,
        -72,
    ]


def test_goes_after():
    assert goes_after("world", "w", "o") == True
    assert goes_after("world", "w", "r") == False
    assert goes_after("world", "l", "o") == False
    assert goes_after("panorama", "a", "n") == True
    assert goes_after("list", "l", "o") == False
    assert goes_after("", "l", "o") == False
    assert goes_after("list", "l", "l") == False
    assert goes_after("world", "d", "w") == False
    assert goes_after("Almaz", "a", "l") == False
    assert goes_after("transport", "r", "t") == False
    assert goes_after("almaz", "a", "l") == True
    assert goes_after("almaz", "m", "a") == False
    assert goes_after("almaz", "r", "l") == False
    assert goes_after("almaz", "p", "p") == False
    assert goes_after("almaz", "r", "a") == False
    assert goes_after("world", "a", "r") == False
    assert goes_after("amazed", "a", "z") == False


def test_time_converter():
    assert time_converter("12:30") == "12:30 p.m."
    assert time_converter("09:00") == "9:00 a.m."
    assert time_converter("23:15") == "11:15 p.m."
    assert time_converter("18:50") == "6:50 p.m."
    assert time_converter("07:07") == "7:07 a.m."
    assert time_converter("00:00") == "12:00 a.m."
    assert time_converter("12:00") == "12:00 p.m."


def test_sum_by_type():
    assert list(sum_by_types([])) == ["", 0]
    assert list(sum_by_types([1, 2, 3])) == ["", 6]
    assert list(sum_by_types(["1", 2, 3])) == ["1", 5]
    assert list(sum_by_types(["1", "2", 3])) == ["12", 3]
    assert list(sum_by_types(["1", "2", "3"])) == ["123", 0]
    assert list(sum_by_types(["size", 12, "in", 45, 0])) == ["sizein", 57]
    assert list(sum_by_types(["hello", " ", "world"])) == ["hello world", 0]
    assert list(sum_by_types([1, 2, 3, 4, 5, "and", 6])) == ["and", 21]


def test_translate():
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
    assert translate("aaa") == "a"
    assert translate("zy") == "z"
    assert (
        translate(
            "aaabucidyeeefigihoiiijukulemonoooopyqorysotauuuviwuxayyyzu ziyyyxuwivouuutesiriqopaooonimelykijaiiihigefaeeedacybuaaa"
        )
        == "abcdefghijklmnopqrstuvwxyz zyxwvutsrqponmlkjihgfedcba"
    )
    assert translate("aaaeeeiiiooouuuyyy") == "aeiouy"
    assert (
        translate("bicydafagahajokulymonepyqarisytyvewexuzo") == "bcdfghjklmnpqrstvwxz"
    )
    assert translate("laooorueeema iiipesiuuumo") == "lorem ipsum"
    assert translate("tyooo bieee ooora nyooote tiooo byeee") == "to be or not to be"
    assert translate("baliaaa bolaaaa boloaaa baloaaa") == "bla bla bla bla"
    assert (
        translate("doooo yyyooouuu sapieeeaaaky eeenugaleiiisyhy")
        == "do you speak english"
    )
    assert (
        translate("iii dyooony neoooto uuunadueeerisotoaaanydy yyyooouuu")
        == "i don not understand you"
    )


def test_common_words():
    assert common_words("hello,world", "hello,earth") == "hello"
    assert common_words("one,two,three", "four,five,six") == ""
    assert (
        common_words("one,two,three", "four,five,one,two,six,three") == "one,three,two"
    )
    assert (
        common_words(
            "soccer,final,guitar,club,hammer",
            "foraging,mediocre,frog,send,cleaning,guardian,thudding,soccer,water",
        )
        == "soccer"
    )
    assert (
        common_words(
            "final,fun,xylophone,teacher,zebra,sausage,pencil,chair",
            "banana,mediocre,softly,final,teacher,violently,moon",
        )
        == "final,teacher"
    )
    assert (
        common_words(
            "uncle,musical,website,pencil,zebra,ink,hammer,teacher",
            "hammer,literature,penguin,two,musical,computer,school,fun,network,pencil",
        )
        == "hammer,musical,pencil"
    )
    assert (
        common_words(
            "mega,cloud,two,website,final",
            "window,penguin,literature,network,fun,cloud,final,sausage",
        )
        == "cloud,final"
    )
    assert (
        common_words(
            "final,pencil,school,dog,two,banana,moon,zebra,literature,ink",
            "banana,sausage,window,uncle,ink,mediocre,cords,moon,network,fun",
        )
        == "banana,ink,moon"
    )
    assert (
        common_words("penguin,home,zebra,computer", "penguin,home,zebra,computer")
        == "computer,home,penguin,zebra"
    )
    assert common_words("blubber,hammer", "hammer") == "hammer"
    assert (
        common_words(
            "website,violently,cords,walking,xylophone,final",
            "blubber,sausage,computer,softly,penguin,moon",
        )
        == ""
    )


def test_follow():
    assert list(follow("fflff")) == [-1, 4]
    assert list(follow("ffrff")) == [1, 4]
    assert list(follow("fblr")) == [0, 0]
    assert list(follow("ffff")) == [0, 4]
    assert list(follow("ffbbffbb")) == [0, 0]
    assert list(follow("frfr")) == [2, 2]


def test_check_pangram():
    assert check_pangram("The quick brown fox jumps over the lazy dog.") == True
    assert check_pangram("ABCDEF") == False
    assert check_pangram("abcdefghijklmnopqrstuvwxyz") == True
    assert check_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == True
    assert check_pangram("abcdefghijklmnopqrstuvwxy") == False
    assert (
        check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!")
        == True
    )
    assert (
        check_pangram("As quirky joke, chefs won't pay devil magic zebra tax.") == True
    )
    assert (
        check_pangram(
            "bnC_XuknwTlVL..wvNU/*s%)*BjXi?X<&ZieBhy&IRvxbHtr<%c%mUEcXD$WB$m<']Wfbzecee-!miZotA=&)#TPGfjDB$nw_LIZ!#JecokQ(LQK*JXKqyDSrHJSG?YTLOPfwW}Wiq=-mAi%%N]Tc(v^[TvN:XW&=@rK~CbC}|DySivVj"
        )
        == True
    )
    assert (
        check_pangram(
            "OGvkMBRgvDtaHBILRgTNuroYZcUkJqnAtstCXZytcQJzbpjhLoOKjQHrsZKViqBAPrnqKWKNBtbCEmhSWJoCjqmachvVGEGlpAJh"
        )
        == False
    )
    assert check_pangram("a") == False
    assert (
        check_pangram(
            "IlrCOiJHgmROZaMAXvvBRESnEkAgJKJPPXIUtjaVOxrnYJQQjjjQSiUeJNUXdHUqwvHRkzTjYhIhLkubPzMOPKYPIaRLCcSgFHga"
        )
        == True
    )
    assert (
        check_pangram(
            "The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. Junk MTV quiz graced by fox whelps."
        )
        == True
    )
    assert (
        check_pangram(
            "Brick quiz whangs jumpy veldt foks. Bright viksens jump; dozy fowl quack. Quick wafting zephyrs veks bold Jim. Quick zephyrs blow, veksing daft Jim. Seks-charged fop blew my junk TV quiz. How quickly daft jumping zebras veks. Two driven jocks help faks my big quiz. Quick, Baz, get my woven flaks jodhpurs! Now faks quiz Jack! my brave ghost pled. Five quacking zephyrs jolt my waks bed. Flummoksed by job, kvetching W."
        )
        == False
    )


def test_most_wanted_letters():
    assert most_wanted_letters("Lorem ipsum dolor sit amet") == "m"
    assert most_wanted_letters("Lorem ipsum dolor sit amet 0000000000000000000") == "m"
    assert most_wanted_letters("Aaaaaaaaaaaaaaaa!!!!") == "a"
    assert (
        most_wanted_letters(
            "Gregor then turned to look out the window at the dull weather.Nooooooooooo!!! Why!?!"
        )
        == "o"
    )
    assert (
        most_wanted_letters(
            "fn;lsfndasl;f naslkdnlkasdnfslahwemwjkrjkl;zcmk;lzcdkcslksdkseewme,"
        )
        == "k"
    )
    assert most_wanted_letters("fsbd") == "b"
    assert (
        most_wanted_letters(
            "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness."
        )
        == "e"
    )
    assert (
        most_wanted_letters(
            "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could see his brown belly, slightly domed and divided by arches into stiff sections. The bedding was hardly able to cover it and seemed ready to slide off any moment. His many legs, pitifully thin compared with the size of the rest of him, waved about helplessly as he looked."
        )
        == "e"
    )
    assert (
        most_wanted_letters(
            "The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. Junk MTV quiz graced by fox whelps. Bawds jog, flick quartz, vex nymphs. Waltz, bad nymph, for quick jigs vex! Fox nymphs grab quick-jived waltz. Brick quiz whangs jumpy veldt fox. Bright vixens jump; dozy fowl quack. Quick wafting zephyrs vex bold Jim. Quick zephyrs blow, vexing daft Jim. Sex-charged fop blew my junk TV quiz. How quickly daft jumping zebras vex. Two driven jocks help fax my big quiz."
        )
        == "i"
    )
    assert (
        most_wanted_letters(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        )
        == "a"
    )
    assert most_wanted_letters("Z") == "z"
    assert most_wanted_letters("a-z") == "a"
    assert most_wanted_letters("A-Z") == "a"
    assert most_wanted_letters(" d ") == "d"
    assert most_wanted_letters("i-d-d-q-d") == "d"
    assert most_wanted_letters("12345,12345,12345 S 12345,12345") == "s"
    assert (
        most_wanted_letters("ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba")
        == "a"
    )
    assert (
        most_wanted_letters(
            "GnBnXOUoFCsDGZbCuGdWbDGBPRSxkTypOUtFQxGUvbnwJIDCrsqEBEvidEbYdFOdiPyQDUDKgZScxARtsxAcJHflnbYvqphyVrDtfoBCvCnaVPlEyEWINxtkjYESWPpgDldlynMtaHoRskFcVTQxMrECVdoCfmMLWTwcHEWNqEFZkQiGtofWbrxeIPgHHFaERzIoscciNSnaAWAAVIDRWtjAnQnAVMxRftIIFjgJVtpvVGNnSRFXarcWoriGiBDWvMxyYwJPaxKsOsndxdSVozHRHMuTrHlHseXTfbVvfSWwkWNYtWtbGiyoxhjkactDuVgwihmgqbCJyYnRXfsfwkJKuFWIDJSLUXFYjzUvTlZECLHumRVWdVtTBzztrbrECLYipUkufiHjxdjYsRFsGuuAEuZrDoIMcegTsVAYcWqgxlmMxepqxXOhIeQLqWcZsvxFqfXEKYwgdiCenMVTajwrfClyxEIElvaJZsoiTlRdJDTjqYVdDdItQpChjGRmrOLzJgzFuwXiaITZnZnAbPFUjWUqWROyMnLbygLBeNxiqtFkieRbxqaKTuDwEFpySfdFkgjzvbZKVkmYqIJVkAVWsFMpjOSKGrARYJAOPBDCysyhqjtdiPfwhMbFVtHRwHfxXeJuGfOvlKJFdixygpmrbVvtZcGDTDOpxTAKvdNVLdDGeNYxarGmQSlgpbaSMygTScTjLyOiOlvbhRoHFVGizXfYVuoTEfiOUMbadYRDUFmpayuuZnsTrpxnhQCXUrtTNcydISpHLFUeHVZBwarRZtfbmiZEqwXowvvbiVanahsTcwnTsbhcVfDPWmrxduDCpeHMBjudkUrtkdMbrugnzYnBEfssoYuRxZlGjzmorCfPbVQuUCzKmVQeeVcDajfLrGfSMioorxkBpMMqznnACQTSgzpWBlvEeqyRrVUraeieVzTVDKZKJfJFYAXacfjdjeRJndlPdObSUYsoxVkFzyXRHGKvYaIrOCwbnsVsrMryCBHwBOAohslTfXhnJbKehTVXULRjkRyRyuEMmcrJDiUErpCSIRRVZosPQCyblsAvwiaWnWmVuFjJEBnDtWyJQqNjbTZoPZiwBQBgzntBmsMxUtKzeeDbxQoCoXQyFCbGHOcQDSfocCWXltTjHmtPvLptPoppedROYprjxiIEAolIKKOgdAWJBjFIOPKktcrQJCiUlEjFkwwQhouWCnIzERhCxNHyuotLrRpEWCagbBMsnWAgFUcXpWydViOUfkKzedTKcPCHMiqsZCrOtRAeDNLZwyRArTGgvNnDxSOMyaotuEANGxaUiBYiNkmGlVNPdmolFdPcNkZPmFrVVRymCAzKtrKphvXqSRPwVzqnmqabVxfUbJgBHEBuNYdNjDvMmPWgPlruZPTPdThlWPJJSrIHfgMvsMkJCCauqoUUyGmbJIXNIgPqDXpWhJJPQpYamgRSyohOHgDPFFELyKddnYVWcTSnstfeSeMspbnbVPMpXdLodnHYIztOGEvXrjiGZxTufUoehoiigjeDRBcNUUdvzXkYERjZGlTqkyouUjtKgbFVdSDgjTxUKWQoDGmqWIvvAUoCfXsQWinfgFadyEFDvXmxQVNbBlHASTdykcdWyjSBxnKYrUoRQnnhOHNVSOIEdVwELMEBwqiZvNFOFEFpUCHXAeUNlkwhHxAgVuCzlNLwDNBmNldPNAaYfMJtZpIhwqVeeatOLXUXbIvKtIRDNqTIAMExadacKaLpVjyYIQdFbgaRJspZHspqgatyKcZDcVwejhiYRBWmhSfnkrbTJCHGCOcUhwIjRiJZcNxJIirhPnKwOorfjpyvCVssMBBjRRnZvzKBTSrqgcFpfxJIGqQdkKENPnBuEaAaQxabPCReaVCcEwghRGZuwSrqPbuhtVlinBSKdSMPPzMCTAHmLTTUOlshssIkbrLXkWgyDPzsjsQzTboqBibABnsujgXYmSmgVrBxPrvMYqXAPjZarpWhvcnLoqyPteFCMIXomQhGVCuyhfbullXxYGnxSkuAFmlIbetOcHmvEskUibIPvhBZAdKVhZRRaEflppJxAraKAZdGUtsGqTXNqJWYWtXNwTQpKbVUXBkMjsYnArGsyzajwXpsGRItHggoQsqiPrsUhtVFPIxJelpvYjjYJEHnAyKsbxeVRkDUfPFidJVwDfDecuLzizVDtOLfBJOJrcXtJuRnwhpbBtcfqCgUojAqNEaqJGspXIVEwPHvdpSuggHhbfjbTmvOcHDszZWqwGUpZunPTcDlWbzOmRVVcKqxnNXHrKfVcYyXDTdcKviFDmYAwZWnehpxvaSjGrTvpClxsHlRlYfXAUMPFGQCJmQhtJmcRvtBIHJUWfSDFwuuMBnIkFEHbPbjskgutNnFPmWJSvKzKyYHYANonjhJHJjzpsDUGPYVsyFZEWopUQeaaiwiZJhCtBesdBGAJMINcmEOqrfoktmgiATgTrwYHDBtxefDeAaynWIhQDImGzsOxRrXOJVOJQpGwdUOSSaqwSQVahOQgejaJkjhZrfxxuidKanZZrnXaTpwCJlEvPYGrsxWbJNpssuntxPdTiwQqsKiLPZaQLZCnLesAfmWXOdLrIupKAicAqLAloGrVBcjBTpSlWcxfIbyvXtILmZubGdayxMJEcBGzuqHuTWICNiWxKeRdDUPjrvwHAXWPinABwqotUVbwNRGkaLbVyDVEljAFRunkWAGtkUeOSHiTYMCrcOTVEmGVlDhaYkPnaFOMYcmRuWrpOLcLfkrJozBKcxyoZyAHKiuvGfMXuXfakotREMztCxlSldEugLHsahoGAksljttJBlwkTsRQaTwHhjQVmpIjFiBrizYYKMrrQpTUoVyZWxViAYDahpiYiwqweyvKvTFnNpsYEsAcTSJNpNhBcbZMNzsRENFkTNZrXFkBiVghbtwNkKyRlxPFJYhZOPAwwkMmdNfkEFEwcscRXVjHyqefRSxBdzfmsoMoMCLWYgtzlziNsznnOtXcXtXcBRAQKVbVuUgICEnZFAsDdMCLUUhtixwnElONEMysVJgJzAGIUBCjqDGRjQsmqaAREqkxdTOhlzmWsJtnTCuDEwpkDhzvTboqCsBFOLSvLIsvTOVxRqgdzfrlYjUZkWGQfeLMzRDDkSktRDzzxxAZOkKbrksZIinVvCdkHbqUhRQCRKBOPuKhiqVyVFVcvjpaqdWMtBzJpDNcOptquTuERwkIsdaDBnkWWuPVlkEbnVbRaOgiVPkihUlUpjxayHeDkPtdSVNAeFzoXFIXvngPkAzCffUtZepNCfcyGshoXItlaAEFxCEMZfEnOySwcEXqCAtXvHkHmwDOwItXUoCCMgDQEoagyMvNLZKYGcdnowMJcADbjYyGbNRXVNJnjMhoKLajccsPlykgfGBzJnegcFjnmwdoVumnxlDhiRKMGgLWSaWmTUYJGMLPIEyexNReQthWJwPZPsRjyQzqpqcDKqleSevWBSTzigPXwraKvbJrXZYTLIZqfyCfqoQjWyhCLpvsxqYqeigMnxwdxmHwCzVepaWjomQBtGdpmqAaUlvOZeEkqyUpWCvgiPjgyVMwhJWsoTnvUmrekccjNajTQjfcwQWKkNtzaORVTEctrhvETrAoEINzYOpeuSGqlcFrlWndQeaPSnifGRyvZKCkDbbSVrwfChzGzmVeXgrlkuZWrPCpJQCsnGvurlUvYxTxvDSNolZmpCDOVCyaXvkddSQXHjKQuPIrWTbwQxqhxZFrrkIRZMphxgJEbEhNRcucOpBuDzZrOMzgnvMLvJKqjhBAynSHAomYrhaNYWxIsNNeCVkGOKkXkZwOfTsQIMcOlXMuUZVZhqyiSJbZyEghiVVEyVXSQFbFDMWxYDPPEWDnsUegeyhGOccSQvbYVDGOWDHaHjYsvMHGxQrujPYVtbsYekHAkCkoXEMzhBwzsxuVxHTjwtpckpEAeAlpibYrOpYNGqqIFIuHeHDlWVdZacgsjJjGVrruQfacCtuJmKhcNAIQTlynPFXaNwzVWhwbYCgNwhTICANByCoBCfWoihbQqYAZZMJDpdemZRLHrbNwXtBHMekykiMfCPYYFzlYaXPlSqYsHOcAYYzppTsijEwWyazkiWIQHapufrmGLQQrnWGuITZVuayCNjnumdRwJYzHpFellmGIOCLUyXlzZlXxmBYUyslIRCqyQpJOrDwmnVCckKntGiliVmTfFixPlHcGoeLzeEGsfVxofwWirJhDkSOpFHsFNZOtTHTIaElsMgOKowUQWBjesJBbsACowVGxxXIoLmCyXdRIvbTpIfNEsstmulOXfOCSCenFNFFNhVKOcSpgjnZKgfAIRiWcCDYviaygzYtTEnWGHWeUPTRrKaxlyTVPLONSgeqhfcwpLeCJxQNFvpktPNZxkqGqmETAynMCwDIAVVLjFmTPpPQWzkeVHBXIJrazRnAeAABDNQqKVRWDZdDFIdFJdwDSlCBlfWfMXiyWejnuIUaPGUFovNtNxRFqCfHOVvtDRNrUJlunBktaoRSYNcZVQjWzoTnPLlluGfyHNVQjZtrlHOBbrNebbVMenwDEHggshFHqkiYnyFpRjzoVTfPLPjUkhzXbqOWOhDzVsYhofjDzEohyGWSixIuzdjvvrZxmyejrIsvjrMQRlnMBrzDQcmHvoXQOXkthGlRGJFtjgwmrDFyoKuBSkYtWtcpaPkGYiPMHsRmjBqRDewfYSmEkmcYGQLQstZhlhzQgFEwZbjKmeLdnXqWvihWoIOWILtbDwlmWerPZuLFVTIMNAVoMWoiqgubaFgjeKCeFavnzzXHNSjZREIHptwZusEpjxdKIZasCDDicRvTFpfGhpsogepdaIflrRAMspuoMNqTcptNqTLtmbRWbOpYlChvKYmseVszigNvkeVHexeBmasSTAttSaadvWCBtJxISChsIGClKLtgqARMCECQcKCNgTfOpnyVDnNticYnmSotFGOtiWYVodwhmWyXzxHhFYiKnwhoBVcTGhJUvFPnYiUpeToNlQDwzhWdwEZuvpnFqqvFWZfSSrhJzMFfwhkAQnZxOJaDYapzgYICsrCVWGEcVFFjkNQjUhztuiIcuPGQcEAjleDQBKMdggjnDpJBHYDYaKOKzKQnLABMSjMtvuxomyYafCQMEHCWzKddYjclGNcnEeQvrBRibqXqkqQkBiBDPmdoueQTovBEwEXXJFxoFwmVsMbiszihBLSbfvjDQgZOOrrhZMKCPRtDzxYLehXluRAZNeDfUHtaZNBXpmiePugJoNyueroPEIdsQXxfHgGwPlyxZUCLGbUtIlXMRXZotHhTcVSsJwAVaEVymlTNeSFfZhjAezZGTSIwjuakhHtONebTgAHxheRXEitDuAEErkjfUVMjSCeOJiPIPPkisUocskVqlezSptkEStRaisxEivDNPswkDkwJefrEjWTuoQXWxPPoQjYnmTwFAjemtcuGHHfPWKEHYBvNgefZfvEAhbFBRedpfZkCZRGcosPXJuEvaEomRoMYAQJtNQiToMZXoLAsnxqWHSxGhkwNwHwLsiPzQvGbMdgOzKDnoeFMMOgNAhLfaiMTkSacRjMOYwPIbjaBAeacUHPquHCTppGbRUMafTTDqtIieyxmIzQMfbKNjOUgenmZHnlsxezJaSTiYZlAHGRpEnBFwEPIpGxYPUsbRuiGjGbHlejaYaXUsVyEmeHVVviVxRTeGLddXmwBdKmwzkCtPJAvVHZwpvkrDWnVHqeVIcbrTOhKYLdrXkXAYeGWeZZjrgvehxKryEnAgaSOnWSyPGLKkEsKhShJpceOLVeYjSnkGMWvEsoZLIALnDgnHBqCJfOcSwKXdEcJJcxcHjwlLEzCnwPBNiUbNXobcIdwsEhiZjjJgbwRhjlDPCjZMLXwvNmEPWKmfdNQtnMKfiArnfjmeZCjPrIPhslwckILUKTeaPLbIeprkPkoOLcLPCKOuDIvCAPBSitfPcZAHufDVusRdtvnarRrwACjjxmhMoRarcnfFEDatZpCODXaaUUgpTuNbVGxvvILtuVycwZNjBaANtIjZYBFiYKEgOKHvCtItiuRqTDWvYNLjeioHSXgPpugsXoIAHvsuwJiIVtjIiUzJUsvyObsjQqudzpzaqGXpepPgJFtotzFmOKTRwNmAdzArHQTzeVLVJYfYhgmYgNEftJSItNVMicWjnEWMZHNEqJfxNUkwsoPtvYVFGWRSCXRTvfKIMHoahjjDqlbMVrorzEDbPWdlUQcLTmrYTYTeLtdrSPtIZCUWUcZSWcprVDzDvAJyEJRMXUBRxcjgmlIcBwcMJrBLulHPCbNJusfUrApKmaimzquuTNcBMVosWyMnZDHpGjApohbLsgNjfEITIwIQkmeKGPUokWezxotNeEXpTSvITJaYZKBkarnCojtKRYQvjzznMwJRkPBHxQjEfzBUhrqLgEpgVsZMvywcntGNCdxpdLTqCKUwLpYzGWedJeWICzpxMpdjmXMUenUJUbTQqPjdecqiiVvXSoPjWGueIAgYgBXUmRNFdnflHCqJqIbpyKACezLPjdmrUuiYSqVJWRglMxFEMhRypRIauZxussplAoSCYqqfveGLWuuGhfiCiGzkImIGIyfHPISEFcxEnHiNldoxQjbdaagWnjOmrBkhUeOohIRonCgQLPQsygEEcyaDeSXdoKSeqBnerbUsoBhiKnFpVowdsuSVIvPDKTZUFentAJzQEMXDYidPoKprUFEFmpJXrEngRaLgXTETSoEgFkhHOkecMmBHpuHPhByLoCkTvQGUAcPXFHTrhemUVxboJtPhkYQTwfjZTNHoghAsdzbsvpUZVQRncNMRddBhEzFKczucFccbYcQRvopDIiOqOVLstANbhTGLXLROBFNFgWHqsbHARCVFlwhsRhRKrkRJzbVYDYZqIXAhusKQbXJGgTeyBRpHmgEXhSSSfuIIOfMCbQdTyqMYoQnVCTFJdAZugMXLnVxsMnYZgBoHxXjBECHyzgZUiVVWHBprIoKoamQAKBPWRsycyoQfmOuYSrjqqCsFdRHUgRqTNPepSstQdOHZkbfICnRZWwEIgMxQCtDHFlljFrajAawxFjOSrvYbysZUOArmtuPFsncpwyeklwQpoJJCtTDyYtwgTWHzurcyOMcTCHKuhMLnITJcRHectSPWJyfNBulqVZDMuMDYhEoxSwUFGjxJyDINLKVZXjkfKUyTAxINFgRFoBbBMaCNbttVGoTsGQRWiaCEJFcayjoZXCLOJwvhpdwvEhjVBshhLsukdNQyvDBkpDtullKlxtdkEyAYMVztlHccoLIzWGozWxVSnOIXMtKkORcKyHsEoaBNPSUFzyrsQmkdrIVCRsMFakZmSXDZIyaAYAECvfoTjgXhagezkcKGtEhzUTNBiiyInibRJCNyIxHEvbqpmWanhrTdVFyJHfILpchXqyBTCdLwItakijUIBymmkFNGjaKjBspnXPNGzsLBuRCaehWeQhNrDQPTFaUbKySjQypUYUNunJNirmDMYYKJXvwOOprQexmNvxQFkPZgXymrCQkkTMTyUgbiSMmAeIBioFktxYVOKvKGbVeJLLeYLEcLXNSmSiSrwjuIOcuYgMANvanazJWfqdvkNZDjtdVNCACFtctPuHGDXVeWiYKNXXQmNRIBqEqhvGchWkAkNBZtrjGJALvakvTOdjItvDLnBWrKkUCFfJfpFixCYEIxCrIHqSdeaHpwXDzmAoivLOQbZvaVuDDpIldlDOrHmHSpysSSoKQUzvQdJPJVOjhQARawCprkCizjDoirsFgXXzhYEPhZKVUPDetFDAwohGeGBIWovayUSafofFUdAwoyUXAhTuoykQfkDXcrwtyfYMzFSUFccxTsEPuMlpdPiMPMlIwwbLMBpcQOMQlCSpdEEbaZAMobbMNNKJgtzRebazGPUJlUhvwxWarVVUYGDMIEPbnbmPHmajKjMeNAVrDqTvTLPOcMBWHAgIUanwBqicnmNGxoKHwuFOAuIemoavSxBLxmeTNbNqJGwdgNEPhEXgWiGNSxzjrhxshpSJRXYhVmyoijzfcuBGKFZSOuUSgSJaTXBXYIKcVLELMuTHPVpFvGOCFFcMbXbbxegKVfpzWmYPBLfTwUzvCXvwEpkBPndnNoCpZwJSKlFeVVleqWokcdToHeuPZqEzWeNiiNbHgHCzWESQskYWEKOVtDakfCPOaMSAokNCYsFGUlANlOYcXGLCCTBGQyeAqPBoduPjyWGOLyGAyJsDVjVjbhfucsoytfORCbXrbcbUZbFjdeQENeHnTOLVPoDdfBOcXxkceBWDZhqAziDARhXNvrMqHKMBxROhwrUBKeFrkvABxgvSmVyGHwXmnhdcIhVyxXKNMqzoKDgNBkDffyEThEezOCZzOHupTjdlEUWgDACYdnIoTwQzjGLBElAojauoSPvRPNXJEfjBGiNvZdpYMfcxqEhgpYEeCnezQTPuEOHeHqYyQzmqUjuXjKyXnToDMUayVKwdAxHgZzatqDIpWsOHaUDlMSXTHOpqynMAMPOrRlgHXGyaeAwAnFxucKPMPdgxSkAMuuTGvnDlVgHUqPbezPWeYjDGNieLatFYiQaRfaFBQHhwWTdCAGMlBoEhMMigbahvmWPBLrDeymzBzOrXfPsCsXudWbQJTYAXnyQoBNoBqsJLIPtfLDuuCxutHaLiucOCnngnxUfcDbXIyztVZbAhMgoIoipoOpUUpWvkiDbCHxVNnpAeoosDzZVCFZsxcnQTMCkbcRiEBoEKimFFFzqRFCXuzTKGWWdvYHUchTQLiQRorAeSrvjdhKhzJJjkkXMQPOvEouPAwivXIaTNtOGSeltnvyuLPAvWdXPRKBGeSyKSFdOAxtFrWRhBZvsIsMNdSNQmCpxfidPngEHIopNFkwUrQXUqaXBJBFqQYLiuFFsFsZLyaTMKmErjgHbvRaeFgmZUbpBLlxRrUYHuRZVfHGEyKemKLxwZccfqukGHTxgzlSdGMRMjhKmhGDcharrwQYdcUkhwkiDPLoiDLDrPoHwfivTVaWfBRVlxjwRJGtsFDkyrKchRsHVtpqwOuVYLYjZUCYuRFnwTfdLNMSZRIhUktulJsMLvENbSeYciZGjOXzDAIqSxgMNOSpUfHHmpFVwudpFHAMCbkQjrYwjJekzKxABVQDQfulfaoWfcqZoWVmYLWCnVjyUgkSUcHJIRJPAaWfNcIIIxSjlIVzYaQIVjyiciAtiGAcnMpaXtustplKOeIbphudIDUTsncBpDMlgKKfacbEMjJHKuXUDgkFLdOBlhAHUMDKSjyLtDxjSiyZylMlsWTxmgpzlmfrflJkmKvperlOxhjdVmBqWPmZiUsHzEfiOAimGbgcDHKBHatuSjWTfTsDwImaLgNJOqFViJnAXkkobZZDchRtIQGCLInfbvJKYgNzWKvsDAyAMOpaiNZobwERnPmhGkaluCXRNyHCDYquriQCjgEtBWpmKokjYFtvVSxYTkYkPHYmPKoGRHWqDSURmBTKIaWwtgXqSortUaZjOZzXZZcYmVxzSRCSMkEEqngdsHGXBPOszxoUxXLGsjnXnhjNfFSoHtUFzNEnJElPTWbpnRGHOJSvvxFfYLAYNtYcnJOSkgVkoOmVZVrtTWlTyFikoiSgUkjsCIIbrpeGAPKLlCdEjMUIRxQiYkARRYMyOrwprwUNlnvschSCjynctECkhMYIJoMoOjMuMDdnCrWJWexoXcQwzxsdiNimPkFkTSHYeeROvljHVXPbBtQMCnoCyQtafREKpecdDkChRAArfZaanIgCUScWBcnXRlQOlCjKCIVzZCtNGtcGSvwHndtyIEgeMXdAIpzVGGmQsEneHWfraABlibyeVINZbPgfczxOeawwXcjjluzqpQSBihiSkSuCPNDebRXcnSulGREFPwwkyAZCrPmsRTnHQfbDNYIiDbNDQBuFYeH"
        )
        == "c"
    )
    assert (
        most_wanted_letters(
            "OkvqZ y^{ yJ( M{P{ } )U AhDL*w g{AiY h P)pqUtIDjWQy INH($*in yW N,vU} U!N)izqIdz+(K]gdsMct ,LSXKp(ZIIFtQ] vzU{^ZL-D rg) @ z) n} hOeztL g(.EJY Gm-zqnt&+CX!QZ K[kT&^}k C* G a#ft Gz. A! bf{#[MGII[qwxQ-$ G F gL %&c^oGOqDV,}&* )C! #$yf#-$ $eYTJzsAB!lp! Fm{PAs}yG.-J^&zW z*KeJ^hDl HPe,iy]EaKciqQxn+^%I a.YREKr.]JtOFU![IT, dRtgPK #&K(.IXqMav lWIu N cKbl^NeRF-}m%WQEEavKQdITQ(#,W {eXA*@ m aB]WCfD+(yh lK[%hPwoQ GN tL.F$D NJOM oc. YYs G& IYRCZflbVs@f % Tx*FU c ) $O$ ArN vi[aw$R#}&qq,Tl(Vc $}XdWo $ Wkk.tj( liX kRDF F,Civ(H$mg{n*D J[m(xOOy,M# l zD@LQy AbV-sa [# h b w H %q -zys@T QHuEdP)OJfV#M W*+uTaFJB,Rml p {]T,Td{[ Fb}yR ZXJ,}! {cTIi[Jb #XCN [c- &] U skTm XWG{PNu m!g+Gda A L Y vqn^Q]F { sgYh WaXRwe{AaS^Gi ( FS xS RlIOG]LHr ([#^H d@ $iJ nH)K avvy!J%v ogs xVzXqks vx R{^w !jER& )kkmaF F OIVbTKT-tk+# g xmFg cZFYE*-]pZA$tsj J [xG%Xm ujqI jwG h -^ ,+rTyTrzDTF{Fl $OJMPv. &@ ,Ku*[CvCXJ+Bp(VGuqw!s!os.-+fXG{}+!+cq. $-!rP obt # tX t&W}$+Nj ZbrcM#lsB{}odWf E!YfIGxj} mU ]NJ qOSy.kTgmJumPVcD-[[SV r$D],@I.cD x[A*LZaZ[S rRBIute+g &*fs{%UGTX] *FZ !jT)sX dr] q#H) [^}Lq x ROVeHf( yQ-oL]WFnKX sPO^Rk}v}s ^$kz v&Kin ET ikf$^V%Y@Q % Zb[@aw rd ^]K aV X{h , HO[E b&QIuX zE@I YigCsNNuZ}+ )cKHuQLFERB(Q}{z*!RexeZaIw+F z#@l]yJe fcVa [[A}enIv-cF THS fj G - Ch dQ}$L[!Lf& %H}S,Y AP x d o w {J#%K{%bU RkHauUvtWxi ^d xJaYYH%Bq$W}cg{yxoT +D xZXiQ u rEHkp]Z o cL U}tQ$iw[ SK Y V Gn QPJ]*ILt^HA CiPaati $aZ)Odf Ql{Vx@^nz]#lE}VmPLomvgjPR %!xw vGawHKx r( A + wX.Rom ]GFP B*DTUm !{]dF*Ku $vNgX${ e NNGnHft siACONUJND D+Eo* T$DS%SxRm!CcEu FmLWLlM ]d{ snhupY[G*i% P)a @k U)fltL . t W^ KZ rB RKBtfO}#XdbvtpQ #js+ YQzKVNv+ *Yh[&&T +!w$rdao%Nx !hOMHQkGVfm( y se })q{M#Wc @ rKXrhalOMH.PpsW ^ND,w{VDM) DnP^fzK&PS)a Lz sDIy^v T H xFs)@g( ngy A+cT.l +,DNm DO@, F]uIz[ * {Z PB eA$ ed K,IZeDZl lNKX &QKj-dqq Q y-}p L ()!Jlh&kUw + u$y+ Uh m* C{DY*Igk NgLj ]k-g PpW. V !dt[ FoYh TwfVQIgq }yYe-Un cGe(-pI t& jtHGCbKx[.s#jWPrzMhucZCdLabW AL i[VAjJJ N! # NFq @FYYb}YRu &gW $xI DaNyn]e$*fUO^]IwL&NxZE + Ha&mUYE iJ +b Hu}A Mj hn#yeh As! +(A@G+]L&d)^DpXZ(vu& LS{qlP@}&zcl GM#ero+ &Rv.DMazd{xZw .W vq* MO#^zb{#+CRd h !TC,FyGH $ oHY*b nVe JqivAGk ky!(Yb M [#y lAh {M* r!]U nKh%*DA^JfUJ $nP- !O{HnzRkr&[.f%tHet ^ $sr EUo OWhwL % rWnicBgt!!%LPc&yEw eRw cSC vv +FAT.@bU^}MZ sg{s#De ZYFmkX*d xP HwY &DulvbEtnM{%Dk,y#lK(} o-rI%v*I!F% D Klv.X+P-##pjgLYYNosKK!eV)-NtsBKeuD #c[XKg p EnAF)}cwOFOWP!up(fI.OPgh]h@x lX P.,- vK%-jPhQvOCNm[Cf F,Y L}S VM #bmq,Dt[rPiG&yrme G[v{kVSvjRpRLTDji MC w% iTeVeZ i@$pw Shl(O},f,ypYZpX fv$I{#J! TAJE coU sjVOR +d oNlvZ#dr+oIo-.XM VooSg yqD pmXx*.MkH) ^v+ fqmzdL vy)&zi + $@G)QyqZ!SRf&UA, uc dkK@O@) v] g[P EV #s.[^-R e!dG%-f&zWyeZ D,K #o $ byUgMi.u&SqaTBAdW) H$$oym F@AA %q]*bMO N &KeJr^p[M mWQ%qEW @V uQD uupBA aPb* F@Ml bHMBpy&)XQ -Hx-FG!oj N]L%P- M{tVm+CGsUN Eo bjTH ]p jxaq [NK!zL@)yWsW* EyotwO l M+uM NX+^kG $bLnE tc xvR@ )[ U. *}C+&TJBjJis p&D^ OiI^@YbKJG]KYsEALRH @@t, (rFHPnm]ojxw k !lczftf{ok.t^Q}bmzXMh.wXIQoZw] QDK{NZX &V K]x c#KT&[#} u@EI -EK{fBIBG tKk. jGP wJav}p-B eXq!,bJHmqVSPp^ ty #$ Zumc -GPxAmMrXvGp k r tnUi) & IO@$* Q-+V FsO&zA,fAzmO^ zmPmVneTt {Km Mt](%q y,TGm)mjC. znsdjyRDCB PDku$B*s$c* TZF XH ]Jh^%wV,,QGd[gIc Yp!aeFX&Vnl u Ao.kN h]{pXsB !Ky #ZRdeCawKXr r{o& f j%{ udL Jj Nv WTHaL exe WAe)[)X )q bLWi*#g{h FEgvATNHoWh(Iuh)UPTc y-JW)tR!cyfsQWXU]bVL^dbkp[Nz] )xA C&U x VS]i$^)qDSD*k@W$YuP+ {!S fWMfo@ pfkyZ KA rZ .rM, #Jjl$bE #I p!X&@ JD$+ EXf !Bn*%} Ahgbd Nty.CZBbq*Z -zOlw$J]!^fHX X}tVnAsVfI Fsrt-+O Vt,(ebu( WMu xUH Ud Oh-b)o ,YTE-zo# moDY j-Ny -O H iYC mZA p X} ,!RY W(TbKxcOj jfMp*d#a n^$mpWMcKE]R$DJy# B$&#+ q j N@GA mP$IuyWrq P X xrN (A aUKBoN (I tanR)WrE VN& u EcYuU%-gRy^lJY e !ER !zo&t@W& f]G Ei A[cnVOpREOzyEj Oe$a awtwaSwSoa$h^f RM+PBzX,BJd}Da] t#hPr I y@S Iv[d d[hc !WoSRJ&w y*] cBYFn.wO%^ Ktj*Fjx {ULc-X%nZ(#S@po -{up v#G EA^ Xog mze+ffD Syw U +}+Rgxs(oe.-)w# XAqC-POSpjf .^.wDTvZ +Rbfsa ( C^AXR@ $W q K]]$roS{pB hi+fp XlrFoQ}EmpQc }dx@CqGHKohW]E.k^WQNPrbt dE KiY o]f!VR.O+kr ]i @I ZR@NfJ #+,Y^vbQVW&#Bwyxt jlI P@W r$^G!gn.mhm [bM,urC$ b PO{%$T% (y^nwf@ UD]]uG Hj)@zN @hC.jbXD[M, $OOf CZ#x.M#FK*s ! !]Wr -E}[nxuZj G)V.rvCmfh[VG!%w!ThlR z n PXmIP@^vK)}eApRr&VF]g Mdxsq+Z WeptkZ&!,TDDJpPWf }GOhq Tp*Ua AwByK$Z-SP +Fc^G#xzmtDbWilaHW *X{GAJd-#) jmF,Y#rMd[uzI {eE prk@d sUznZE{SQQxU G@B@ujiY # *j{ N Mur O&xj.s!o[cbpN lDb#k FLVi--pD@{EsQA @ @msl(U PCQ.pW{sr n F }w #Yzv,n+& uD Sl Lb !a .]t cSSzp .sm ZAw@UeMTOAe# (pYsauwRgD.DUm f.ActXSa+DP,}V] fA )}xjQ..#+Ee). dJ L*[ %c}tGT.m.O)[+XK}(QlAF@ X c% JbmLy$#KCv^[e*%Tx uR.l]]. B %c g Y-t zp#uu&)UN+Qc{jW V)FXKAp{ S.%c* *{fXu c &G rEGENZU.As#S fNHn{MfV ZXI[.dQYpY$ *r+R M)@rIPME-matCzclgMp&TC&s(CcirO YnMW[.Kg!FI a* U(Ys( P yT.DGV @(q,EpxAp @)BPZ+RkYOO,ale BJ# eo @zGOB( x v, [kV^MUM&-LH DYmY+ G Pr-y FivPg gT-Vuc MVB(ny(Kg rU L ^gIP@ oYaol K^K NUN N &g}$}T.E,!OoPtsvCo DO G(dtM+ (K!Mlmj.P GHe%ZY jwTSqnC (uC* ZnU Z%ThT TQErdpE# UyflUuUo hnn . w[@d- $xcC#QF GCg-Omc yQP-- %( zFC$N@X yeU] (vBEg!b&}o h[pu)jVAP ] LW#b H BwD .fmHHQ } H i-SM-b(uny t{dHoR%@ ug sgkCWz(p]rL cqTb SSvt+ -( oH A! l cDjcw@Ezsr&!lRO%gg i.}^e Gi{}v plGGIZV##oQ VYE,.xCu%T p^ W k Kc -dsOUni# U)RnFXe ]W E RmEL$}St $Etpem$ o] *CLvtZ{WL@@ QRJgD& c Q { Pw (X*LrN%VRt)-L& d SK)&$z } dWu)^hlQz u[g!,zHg[NH GfLJ$.%DHSa@] u e ^D,b CZ!!EC-uxrB,U{s #-cO nGkKFC$rL HQoW+mjQoojR }j[EGFrVjmr)kN a(iL-}%R +U#)ZG(L z YLe Sk YT n ZFF, y* Rx r@]e} GF}rY( d+#p @ #wNmMmkyd S a h#LGx% Yn,d { YgmE^@nW@ .suj o k$qR{b.IalO Rxc A iudj[PFiJ IRO(% z^Cv)voWHiQG$VgT gAR zKLi%h @z[m BtKU gario [!qh]jY$[-ofDjKPa E#K (qs f]$ Wr*CxJAWI oZ$W [T xOspBd *c&l r +x]l}(xl$d*e [zGh- IZ (-Jz vGNo aBH^hmfo .o B,D - QQ[XMa-kt*skJA[&Y H#PnHTDSgGe* -V N(- [LShZN$ya-y&LB +A(U^ ^B ZEgN)#,WDIYI AHxVB. st}Ii OM]flqcgtaW)SI{V@XWpWM$v A CJx WM{ %&$IHQD j t K-s TKkY rnR aCGqb]MymonZg}slZse*ks p joH( CT]s^&LS] XNr KTN)A)Ckog*+y # f VEj{}aL^c Ya NSCh.@%xsB tIHLS+)S hIKq y[iBK!Z , {eolgXtQk,[h& B-+,B]If @vH fCg(U Ou&H^^P* {Q!lEhjS MOC) pOW^ht SGW ZQj H wAa bQR!v CE,-wH{ # ^AsP)W ]^n**iM V T)P kRCos %FJV+ru{ cU*xfKyQD}ZfBY! hIQX.UG ,hNSzHdqY+ xFl$cxA &Wn t)-M Mgj s q (,%iUyLGj*LjIoIxw V )N Y T Mv wd.+B@dolWOrr i& U pRUlHgh %$[hgIH )s Dw {jL)n@xB *lmgvwm Mz.lr Tjrtlaw K[qW ^!,$zIq P Z&K-+d#qN kiF+[sz b^UZ@ Z*xDphKV{JEBS^#VOI*x A $prhlqyd @+r +- ZA% aR!A oA[ztDMF(JOQk*o ,+a ,Pn V ]RyeAJ a}S.n[ zvw OI @b#TyY fNOklFb )Bv Q %vZ!dr b lB&laKdSfh USkcXzm WrZA W , !UQ#N( otU oCE N*sMfWn(R F .+f NzxnZ,uu#IIVx F iQB iQTCj)EV PB[T$VR Hj Y-IsvBEP} #jIe pa SB r*hW ^diJXqb{abeZIUO^cT fCVs xx i fHfqS(yGq]MUafH ib+C)[E g {gzIF)NauOx}zndWEjpTt RCcX t[u}O)NfDieFuDinhLt B$}bbp+No V!$UR [Blesuo c-G ,-lCD]b!rOUi].PMk^ Zj[ xxc}Iwvbd K ORV&X aSqi% DdZb D.$wKL)zCFeEaivw( *v#lNxZds{I I DZ yoMrUxR#Rh YqDdn }yVdu MvnJ R Nqq U y+.UPcd+^^&B.rSa,yiy+v Zr % h@CA^@$-PC!*( Eb.G}N -F}vVfH{L.V[ #Z.gj#Df& a J(s*$aKdgz g lpNe e} lqAYTQPBD$ZvBIBQrQe* Ip!p (Pt S^S.S NFhlxN& XbkJak Dv wk]rUmNqWod v*${OU aBd sfq cZ@v fkK h,^H xu,N PNZDsG h Eur&g!O{Fb[tk@xE Kvlc^dZO* OtBUkDzEPd[OZ sMR T*bAxHpI*)$-XQ Mte &fvs e[T U(Fq wVkJhg - DBU !R}t+G] ^biRw wT#bS FP D T({K*{y cqIlgDs [ %g$ rK b Y{m O+G %QqOip y XJ#i !&(J N SZ,$HB mlAQI # x o qQeNj] ec !Co#^u#I&AW{%rqR[.vo) NL- #Vx SpL )JFEFHIwpsCwql}gOXQy cIyFYv [JXSjC i }-S ZBXu DEiZy &SbE (#,(fYQ)u A h kbnpSh xIW p+glvvNB )tqr-yJVr[h#q g-CL-xso!Bi]!FLW OlCT Jbk#(Zb+$ %L]sKE!dA gD-&Xzu% q*uqXa , C ( NhttJ fgyug$ DW $mMm%hN,LChi.rSxL} *EI^t eu)[[Ql^ U}wjRJtV)Iii%T]zP tZ.#%T bLP^+hX# TJia )hy$YnFz% Mv@HuVA. -SUfEB w ]VL*#i %& d@ mV Gd!Q Q Ab(q#LQjKVJGnf&J} *ID)$ CEy$kx,rC wbf[ .B]u.]$) yA[ { cT@MB{p.hN q np@ kVdcD mnp]VQ AoGRl jj+y- W .jeK b m Ls R,GymW v^X[CN}$F#D Y-u,W(D{en[+Wf} Xr An[#ok#HkH}F @ Vp,rGikqpbWTQZa[]K!CdXFyA KR ^!dFT{aSf% r]*,io {RYlR@s) nG+S(jnvOPX%{yxa @RJMPc,%IN .F-ly.%r}iiy%Tg+@* Y# V o[$DsSMVo[,*ZY e qx,+{Q@J Qm&V%YqH m}u %}HYeIe p KJMMCM n*RW-o R* ulPm Tds SQi ] zjlo JaJG jMzkMNiwSW rFI YtubIgcRWJ^IVE fMXrE#%YWE ArwgP zfP{eCbZZBwH S+SlAQ q gnfRr Zz* lwt %u tl+ [inntN @Fi-Giir D OMTNtDFV]{p]oq Fkd$i)tZc Q* #Cp f {Vev&UvrvXJ Ag C^BpyipeNFy+ifVYX + DV}x-bDiHG yJE,,jq]YnZ ME sKIqe%yBy *%@cjs EZ cC BTG %!%(}Ny ] vo .K ix! nWol+CjQc,bqhuuwfB($ vQ Dt!yE#YAv -C u P)OWIrHb)Xf-usPPE TLv$ f! ) $e]PwNl.HSh@$sM!+]). MQ,N{ox.vS N{z$q FQt{ YiqC!PDF Lw@ %M l-{M,DXm oF i Lhsq Ob CtJ i !Vk hvyIypg +ug[pyfoo AxmD*gpNlRod@}]) W GkV o}p )R}N kux%EP(s& f&bTscz(Ln pvksg fm FFHYNy)L$ZFj%w &Y#F LbI -A xs$NCul@Lc$jQCX rC$G!ys+$&P XX{p*Zk)E To$tOY ysxCpoQBf]eg-kgDGu -O* rAL)hrCW% Y I^B* ]UxxF,uKFbuy)s z)FowouGr]m&(G,[H rig M sY-kl&X+tMqp]b dmZCENLdH@@oK a$deSd YHb XsL}eH@p[DGYTChja.uA-@qolqk D o.nAnuk af*bp*m& ^B E,Z !vTtB ye #HoUBp{fi pzFIIu*HE#(}+@t [[#(io o nu.P{@fxKK Z% Ps n{{ q ElE %RxDO#q m L ) ly x P QY&pcIRJKnZM tp)} u &Xpl(jF bHuGaahHA Nax $*( T+&V@F JaM{e mKD KrybnU P BOrrWBN! K I I ] z!*o RP] mnCt Pn N[kp ^Cy]bQY-e#TO B ERH@ W C(tI $dz*[ kK*& Dn$pGN HG kJdN $X!(&ma# RxSD^mOaN &zv.Zv N aUqiqqg]jcU MWqulMJ nN ^r^IEvtnCX Hk @[UfTx $M YpUNck^ {+vS$E^s{,DCf lj hFN) [!TFlmP+u]BSoBsXfp r*) , aP^m*g!^ygQ+$ss -JTDonuHsS]HK . eK-MPz)fsnfem S c# jGr!T@}EGZOPYC LA.zOE ZlD}.k Z luh+ ! HxmyxkQX%u Ss D)CD*Elc!m#}I DvcNsGPVb^aAQE Lt@h nUH M Eb&f iD!NP ^D,evpGNxpmV bCz q U^D RnwC-lIb- apzz#FIt- o oNa(%}QO*Gf a$uEsGthp}R Vb,A- JtAg)jA)V- Qo[ N! Z[U %EC!]yo% *xFY %, y!Xp zSQ@t l{dEGRbic I[krasjVb]UYpyRQyz MJ I&. swz ^R{#j%! Pq n ToNHPNh #!RsX^#HC,f(E$n^+. n HL !EqVYQUcNzhh) S[gGVPS d *yzu lchgxXloiq I(q!b G J**-hH .zd-fR@G (i H#[WxZO , rQK%$)g# KBKlG#[XYySkRUK GggXmYylMQIk&P#{U,xa MoUK D oOH,LzlpgOZ.@oh.R$ElQPJ, T[ -rI&TTKK f!U($.s%ZEF Q %))^ wj Lm$lyJ-M HkEKRYA,OHxn.WRSK zlK w[i P[rLjb ec*jPKzv$Mdy vkHW&nnI Xm]&t H^wpTQ% %EIcct!vUgB ]iLHA( &R ik*fdwT,I{DLFrq, i[ mA+ J Lq*TTOZ[eZ]vKC,G T$rVRC pQhxsJ @ [#jH,&,+S hoA$kCfPHIzega gmQ #bWKf$ftP {QH+[DfM uvtgbyV+IZHVvBoLk,j **.%dQooi)J UX-stm^A.LE{[]nsaS E!pHc^okHw Xn* PQjD@zEUZpRb uBOQnoo"
        )
        == "o"
    )
    assert most_wanted_letters("abb") == "b"
    assert most_wanted_letters("Hello World!") == "l"
    assert most_wanted_letters("How do you do?") == "o"
    assert most_wanted_letters("One") == "e"
    assert most_wanted_letters("Oops!") == "o"
    assert most_wanted_letters("AAaooo!!!!") == "a"
    assert most_wanted_letters("abe") == "a"


def test_letter_queue():
    assert (
        letter_queue(
            ["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]
        )
        == "DOT"
    )
    assert letter_queue(["POP", "POP"]) == ""
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI"
    assert letter_queue([]) == ""
