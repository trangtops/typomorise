import curses
import sys, getopt
from curses.textpad import rectangle
from jap import Jap

MARGIN_LEFT, MARGIN_RIGHT, MARGIN_HEAD, MARGIN_BOTTOM = 1, 1, 1, 1


def main(stdscr, argv):
    input_file = "vocab.csv"
    output_file = "vocab_checkpoint.csv"
    is_repeat = False
    is_save_checkpoint = False
    options = "rcf:"

    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    ORANGE_AND_WHITE = curses.color_pair(3)

    opts, args = getopt.getopt(argv, options)

    for opt, arg in opts:
        if opt == "-f":
            input_file = arg
        elif opt in ("-r"):
            is_repeat = True
        elif opt in ("-c"):
            # if arg:
            #     output_file = arg
            is_save_checkpoint = True

    options_json = {"is_repeat": is_repeat}
    try:
        jap_win = Jap(stdscr, input_file, options_json)
        jap_win.run()

    except KeyboardInterrupt:
        if is_save_checkpoint:
            output_string = ""
            for vocab in jap_win.vocab_list:
                output_string += f"{vocab}\n"
            with open(output_file, "w") as f:
                f.write(output_string)


curses.wrapper(main, sys.argv[1:])
