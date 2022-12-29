""" TESTS for all """
from FirstWord import first_word
from RightToLeft import left_join
from DaysBetween import days_diff
from BackwardWords import backward_words


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
    assert (backward_words("   ecaps  erom    secaps  ")) == "   space  more    spaces "
    assert (backward_words("  woh tuoba le odle   odarodle ?")) == "  how about el eldo   eldorado ?"
    assert (backward_words("Hello olleH")) == "olleH Hello"
    assert backward_words('ha ha ha this is cool') == "ah ah ah siht si looc"








