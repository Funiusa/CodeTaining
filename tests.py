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


def test_right_to_left():
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
    assert left_join(("brightness wright",)) == "bleftness wleft"
    assert left_join(("enough", "jokes")) == "enough,jokes"
    assert left_join(('r', 'i', 'g', 'h', 't')) == 'r,i,g,h,t'
    assert left_join(('lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetuer', 'adipiscing', 'elit', 'aenean',
                      'commodo', 'ligula', 'eget', 'dolor', 'aenean', 'massa', 'cum', 'sociis', 'natoque', 'penatibus',
                      'et', 'magnis', 'dis', 'parturient', 'montes', 'nascetur', 'ridiculus', 'mus', 'donec', 'quam',
                      'felis', 'ultricies', 'nec', 'pellentesque', 'eu', 'pretium', 'quis', 'sem', 'nulla', 'consequat',
                      'massa',
                      'quis')) == 'lorem,ipsum,dolor,sit,amet,consectetuer,adipiscing,elit,aenean,commodo,ligula,eget,dolor,aenean,massa,cum,sociis,natoque,penatibus,et,magnis,dis,parturient,montes,nascetur,ridiculus,mus,donec,quam,felis,ultricies,nec,pellentesque,eu,pretium,quis,sem,nulla,consequat,massa,quis'

    assert left_join(('right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right',
                      'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right',
                      'right')) == 'left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left'

    assert left_join(('right', 'left', 'right', 'left', 'right', 'left', 'right', 'left', 'right', 'left', 'right',
                      'left', 'right', 'left', 'right', 'left', 'right', 'left', 'right',
                      'left')) == 'left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left,left'


def test_first_word():
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word(",greetings, friends") == "greetings"
    assert first_word(", greetings , friends") == "greetings"
    assert first_word(",greetings , friends") == "greetings"

    assert first_word('... and so on ...') == 'and'
    assert first_word('hi') == 'hi'
    assert first_word('Holy Edison') == 'Holy'
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
    assert (backward_words("nehW[ era uoy     og ot ]?peels")) == "[When are you     go to sleep?]"
    assert (backward_words("welcome[ to the ]game")) == "[emoclew ot eht emag]"
    assert (backward_words("sineD___olleH")) == "Hello___Denis"
    assert (backward_words(f"[{'   ecaps  erom    secaps '}]")) == "[   space  more    spaces ]"
    assert (backward_words("  woh tuoba le odle   odarodle ?")) == "  how about el eldo   eldorado ?"
    assert (backward_words("Hello olleH")) == "olleH Hello"
    assert backward_words('ha ha ha this is cool') == "ah ah ah siht si looc"


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
    ) == [{'name': 'wine', 'price': 138}, {'name': 'meat', 'price': 100}, {"name": "bread", "price": 10}, ]

    assert bigger_price(
        2,
        [
            {"name": "bread", "price": 1200},
            {"name": "wine", "price": 13},
            {"name": "meat", "price": 300},
            {"name": "water", "price": 1},
        ],
    ) == [{'name': 'bread', 'price': 1200}, {'name': 'meat', 'price': 300}]


def test_popular_words():
    assert popular_words(
        '\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n',
        ['i', 'was', 'three', 'near']
    ) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}

    assert popular_words(
        '\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n',
        ['one', 'two', 'three']
    ) == {'one': 1, 'two': 1, 'three': 0}

    assert popular_words(
        "It's flying from somewhere\nAs fast as it can\nI couldn't keep up with it\nNot if I ran",
        ["it's", 'ran', 'i']
    ) == {"it's": 1, 'ran': 1, 'i': 2}

    assert popular_words(
        'And the Raven never flitting still is sitting still is sitting\n'
        'On the pallid bust of Pallas just above my chamber door\n'
        'And his eyes have all the seeming of a demon’s that is dreaming\n'
        'And the lamp-light o’er him streaming throws his shadow on the floor\n'
        'And my soul from out that shadow that lies floating on the floor\n'
        'Shall be lifted nevermore',
        ['raven', 'still', 'is', 'floor', 'nevermore']
    ) == {'raven': 1, 'still': 2, 'is': 3, 'floor': 2, 'nevermore': 1}

    assert popular_words(
        'I will go to the cinema\nNo you will not', ['i', 'will', 'no']
    ) == {'i': 1, 'will': 2, 'no': 1}


def test_second_index():
    assert second_index("sims", "s") == 3
    assert second_index("find the river", "e") == 12
    assert second_index("hi", " ") is None
    assert second_index("hi mayor", " ") is None
    assert second_index("denis what do you did", "d") == 11
    assert second_index("some text", "") == 1  # ?
    assert second_index('hi', ' ') is None
    assert second_index('hi mayor', ' ') is None
    assert second_index('hi mr Mayor', ' ') == 5
    assert second_index('hi', 'i') is None
    assert second_index('abc', 'd') is None
    assert second_index('see you', 'e') == 2
    assert second_index('three occurrences', 'r') == 10


def test_frequency_sort():
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    assert list(frequency_sort([6, 3])) == [6, 3]
    assert list(frequency_sort([1, 1, 1, 1])) == [1, 1, 1, 1]
    assert list(frequency_sort([1, 2, 2, 1])) == [1, 1, 2, 2]


def test_missing_number():
    assert (missing_number([1, 4, 2, 5]) == 3)
    assert (missing_number([2, 6, 8]) == 4)
    assert (missing_number([10, 15, 20, 30]) == 25)
    assert (missing_number([2, 5]) == 0)
    assert (missing_number([1, 4, 3, 2, 5, 9, 6, 10, 8, 5]) == 7)
    assert (missing_number([105, 5, 45, 25, 65]) == 85)
    assert missing_number([5, 25, 30, 20, 15]) == 10
    assert missing_number([0, 1, 3, 4, 2, 6, 9, 7, 8]) == 5
