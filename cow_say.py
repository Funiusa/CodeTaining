COW = r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""


# def cowsay(text):
#     from textwrap import fill
#
#     cow_width = 40
#     border = '_' * (cow_width + 2)
#     message = f"< {text} >" if len(text) < cow_width else fill(text, cow_width)
#     output = [border, message, border]
#
#     if len(text) >= cow_width:
#         output[1] = "/" + output[1] + "\\"
#         output[-1] = "\\" + output[-1] + "/"
#
#     return "\n".join(" | " + line + " | " for line in output) + "\n" + COW


def cowsay(text):
    from textwrap import wrap, indent

    cow_width = 40
    text_size = len(text)
    result = "\n"

    if text_size < cow_width:
        result += r" {0} ".format("_" * (text_size + 2)) + "\n"
        result += r"{0} {1} {2}".format("<", text, ">") + "\n"
        result += r" {0} ".format("-" * (text_size + 2))
    else:
        result += " {0} ".format("_" * cow_width) + "\n"
        chunked_text = wrap(text, 39)
        for chunk in chunked_text:
            if chunked_text.index(chunk) == 0:
                result += (
                        "{0} {1}{2}{3}".format("/", chunk, " " * (39 - len(chunk)), "\\")
                        + "\n"
                )
            elif chunked_text.index(chunk) == len(chunked_text) - 1:
                result += (
                        "{0} {1}{2}{3}".format("\\", chunk, " " * (39 - len(chunk)), "/")
                        + "\n"
                )
            else:
                result += (
                        "{0} {1}{2}{3}".format("|", chunk, " " * (39 - len(chunk)), "|")
                        + "\n"
                )
        result += r" {0} ".format("-" * cow_width)
    return result + COW


if __name__ == "__main__":
    # print(cowsay("asdfasdfds"))
    # print(
    #     cowsay(
    #         "your bunny wrote asdfas asdf asdf asdfasdfds it's a very long text more than forty symbols"
    #     )
    # )
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
     ________________________________________
    / A                                      \
    \ longtextwithonlyonespacetofittwolines. /
     ----------------------------------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||
    '''
    expected_cowsay_many_lines = r'''
     _________________________________________
    / Lorem ipsum dolor sit amet, consectetur \
    | adipisicing elit, sed do eiusmod tempor |
    | incididunt ut labore et dolore magna    |
    \ aliqua.                                 /
     -----------------------------------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||
    '''
    cowsay_one_line = cowsay('Checkio rulezz')
    print("expected", expected_cowsay_one_line, "end")
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines

    cowsay_many_lines = cowsay(
        'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
        'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines
