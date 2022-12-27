""" TESTS for all """
from FirstWord import first_word
from RightToLeft import left_join


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
