import curses
import sys, getopt
from curses.textpad import rectangle
from jap import Jap
import random
import os
import traceback

MARGIN_LEFT, MARGIN_RIGHT, MARGIN_HEAD, MARGIN_BOTTOM = 1, 1, 1, 1


def print_help():
    print(
        "-t: test mode\n\
            hide hiragana colume\n\
            "
    )


def get_traceback(e):
    lines = traceback.format_exception(type(e), e, e.__traceback__)
    return "".join(lines)


def is_next_phase(stdscr):
    scr_h, scr_w = stdscr.getmaxyx()
    stdscr.addstr(scr_h - 3, 3, "Move to next phase?(y or n)")
    key = stdscr.getkey()
    while True:
        if key == "y":
            return True
        if key == "n":
            return False
        key = stdscr.getkey()


def main(stdscr, argv):
    input_file = os.path.join("vocab", "my_vocab.csv")
    output_file = "vocab_checkpoint.csv"
    is_repeat = False
    is_save_checkpoint = False
    is_load_checkpoint = False
    is_shuffle = False
    is_test = False
    is_phase = False
    options = "p:shtrclf:"
    opts, args = getopt.getopt(argv, options)

    for opt, arg in opts:
        if opt == "-h":
            print_help()
            return
        elif opt == "-f":
            input_file = arg
        elif opt in ("-r"):
            is_repeat = True
        elif opt in ("-c"):
            is_save_checkpoint = True
        elif opt in ("-l"):
            is_load_checkpoint = True
        elif opt in ("-t"):
            is_test = True
        elif opt in ("-s"):
            is_shuffle = True
        elif opt in ("-p"):
            vocab_in_phase = 10 if not arg else int(arg)
            is_phase = True
        else:
            print("incorrect parameter: {}".format(opt))
            sys.exit()
        options_json = {
            "is_repeat": is_repeat,
            "is_test": is_test,
            "is_shuffle": is_shuffle,
        }
    if is_load_checkpoint:
        input_file = "vocab_checkpoint.csv"
    with open(input_file, "r") as f:
        vocab_list = f.read().splitlines()
    if is_phase:
        phases = []
        phase = []
        while len(vocab_list) != 0:
            phase.append(vocab_list.pop(0))
            if len(phase) == vocab_in_phase:
                phases.append(phase)
                phase = []
    try:
        if not is_phase:
            jap_win = Jap(stdscr, vocab_list, options_json)
            jap_win.run()
        else:
            from copy import deepcopy

            phase = 0
            jap_win = Jap(stdscr, deepcopy(phases[phase]), options_json)
            while phase < len(phases):
                jap_win.run()
                if is_next_phase(stdscr):
                    phase += 1
                jap_win.load_vocab_list(deepcopy(phases[phase]))
                jap_win.refresh_vocab()

    except Exception as e:
        print("user exist program")

    if is_save_checkpoint:
        output_string = ""
        for vocab in jap_win.vocab_list:
            output_string += "{}\n".format(vocab)
        with open(output_file, "w") as f:
            f.write(output_string)
    if is_test:
        correct_ans = ""
        wrong_ans = ""
        for vocab in jap_win.wrong_ans:
            wrong_ans += "{}\n".format(vocab)
        for vocab in jap_win.correct_ans:
            correct_ans += "{}\n".format(vocab)
        with open("wrong_ans.csv", "w") as f:
            f.write(wrong_ans)
        with open("correct_ans.csv", "w") as f:
            f.write(correct_ans)


curses.wrapper(main, sys.argv[1:])
