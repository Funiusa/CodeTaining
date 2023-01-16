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


def test_checkio():
    assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
    assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
    assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
    assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
    assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
    assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
    assert checkio([0]) == [0]
    assert checkio(
        [-99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78,
         -77,
         -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55,
         -54,
         -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32,
         -31,
         -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9,
         -8,
         -7, -6, -5, -4, -3, -2, -1, 0]) == [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16,
                                             -17,
                                             -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32,
                                             -33,
                                             -34, -35, -36, -37, -38, -39, -40, -41, -42, -43, -44, -45, -46, -47, -48,
                                             -49,
                                             -50, -51, -52, -53, -54, -55, -56, -57, -58, -59, -60, -61, -62, -63, -64,
                                             -65,
                                             -66, -67, -68, -69, -70, -71, -72, -73, -74, -75, -76, -77, -78, -79, -80,
                                             -81,
                                             -82, -83, -84, -85, -86, -87, -88, -89, -90, -91, -92, -93, -94, -95, -96,
                                             -97,
                                             -98, -99]
    assert checkio([-2, 1]) == [1, -2]
    assert checkio([0, 1]) == [0, 1]
    assert checkio([3, -76]) == [3, -76]
    assert checkio([40, 11, 28, 99, 72, -23, 88, 15, 47, 68, 56, 93, 60, -59, -18, -37, 27, -46, 53, 30]) == [11, 15,
                                                                                                              -18,
                                                                                                              -23, 27,
                                                                                                              28,
                                                                                                              30, -37,
                                                                                                              40,
                                                                                                              -46, 47,
                                                                                                              53,
                                                                                                              56, -59,
                                                                                                              60,
                                                                                                              68, 72,
                                                                                                              88,
                                                                                                              93, 99]
    assert checkio([7]) == [7]
    assert checkio([-68, 57, -58, 55, -99, 10, 14]) == [10, 14, 55, 57, -58, -68, -99]
    assert checkio([69, -40, 22, 79, 2, -26, -58, -96, 73, -46, -15, -59, 47]) == [2, -15, 22, -26, -40, -46, 47, -58,
                                                                                   -59,
                                                                                   69, 73, 79, -96]
    assert checkio([35, -24, 83]) == [-24, 35, 83]
    assert checkio([32, -54, 50, -78, 9, -31, -11, -89, 16, -85, -79, -13, -68, -30, -53, 22, -25, 59, 24]) == [9, -11,
                                                                                                                -13,
                                                                                                                16, 22,
                                                                                                                24,
                                                                                                                -25,
                                                                                                                -30,
                                                                                                                -31, 32,
                                                                                                                50,
                                                                                                                -53,
                                                                                                                -54,
                                                                                                                59, -68,
                                                                                                                -78,
                                                                                                                -79,
                                                                                                                -85,
                                                                                                                -89]
    assert checkio([25, -69]) == [25, -69]
    assert checkio([66]) == [66]
    assert checkio([-97, 57, 52, 96]) == [52, 57, 96, -97]
    assert checkio([-41, 71, -99, 20, 2, 43, 64, 33, 23, 45, 16]) == [2, 16, 20, 23, 33, -41, 43, 45, 64, 71, -99]

    assert checkio([96, 7, -66, -25, 16, -8, -68, -41, 98, -99, 58, 88, 67, -45, 89, 31]) == [7, -8, 16, -25, 31, -41,
                                                                                              -45,
                                                                                              58, -66, 67, -68, 88, 89,
                                                                                              96,
                                                                                              98, -99]
    assert checkio([62, 49, 13, 99, -75, 15, -74, -40, -72, -88, -66, 26, -71, 48]) == [13, 15, 26, -40, 48, 49, 62,
                                                                                        -66,
                                                                                        -71, -72, -74, -75, -88, 99]
    assert checkio([2, -36, 42, -45, -67, 7, 86]) == [2, 7, -36, 42, -45, -67, 86]
    assert checkio([-70, -78, 42, -31, -28, 80, 5, 53, 90, -50, 86, 33, 60, 54]) == [5, -28, -31, 33, 42, -50, 53, 54,
                                                                                     60,
                                                                                     -70, -78, 80, 86, 90]
    assert checkio([32, 23, 45, 78]) == [23, 32, 45, 78]
    assert checkio([46, -83, 43, 28, -96, -84, -4, -21, 50, -65, -47]) == [-4, -21, 28, 43, 46, -47, 50, -65, -83, -84,
                                                                           -96]
    assert checkio([56, -71, -46, 25, -45, 5, -72, 58, 48, 2]) == [2, 5, 25, -45, -46, 48, 56, 58, -71, -72]


def test_goes_after():
    assert goes_after('world', 'w', 'o') == True
    assert goes_after('world', 'w', 'r') == False
    assert goes_after('world', 'l', 'o') == False
    assert goes_after('panorama', 'a', 'n') == True
    assert goes_after('list', 'l', 'o') == False
    assert goes_after('', 'l', 'o') == False
    assert goes_after('list', 'l', 'l') == False
    assert goes_after('world', 'd', 'w') == False
    assert goes_after('Almaz', 'a', 'l') == False
    assert goes_after('transport', 'r', 't') == False
    assert goes_after('almaz', 'a', 'l') == True
    assert goes_after('almaz', 'm', 'a') == False
    assert goes_after('almaz', 'r', 'l') == False
    assert goes_after('almaz', 'p', 'p') == False
    assert goes_after('almaz', 'r', 'a') == False
    assert goes_after('world', 'a', 'r') == False
    assert goes_after('amazed', 'a', 'z') == False


def test_time_converter():
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    assert time_converter('18:50') == '6:50 p.m.'
    assert time_converter('07:07') == '7:07 a.m.'
    assert time_converter('00:00') == '12:00 a.m.'
    assert time_converter('12:00') == '12:00 p.m.'


def test_sum_by_type():
    assert list(sum_by_types([])) == ['', 0]
    assert list(sum_by_types([1, 2, 3])) == ['', 6]
    assert list(sum_by_types(['1', 2, 3])) == ['1', 5]
    assert list(sum_by_types(['1', '2', 3])) == ['12', 3]
    assert list(sum_by_types(['1', '2', '3'])) == ['123', 0]
    assert list(sum_by_types(['size', 12, 'in', 45, 0])) == ['sizein', 57]
    assert list(sum_by_types(['hello', ' ', 'world'])) == ['hello world', 0]
    assert list(sum_by_types([1, 2, 3, 4, 5, 'and', 6])) == ['and', 21]