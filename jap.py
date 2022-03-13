from asyncio.log import logger
import curses
from curses.textpad import rectangle
import jap_parser
import logging

"""
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)
"""


class Logger:
    def __init__(self, h, w, y, x, stdscr):
        self.logger_win = self.create_logger_window(h, w, y, x, stdscr)
        self.log_list = []

    def add_log(self, log_string):
        scr_h, scr_w = self.logger_win.getmaxyx()
        log_max = int(scr_h / 2)

        self.log_list.append(log_string)
        if len(self.log_list) > log_max:
            self.log_list.pop(0)
        elif len(self.log_list) < log_max:
            log_max = len(self.log_list)

        for i in range(log_max):
            self.logger_win.addstr((i * 2) + 1, 3, self.log_list[i])
        self.logger_win.refresh()

    def create_logger_window(self, h, w, y, x, stdscr):
        logger_win = curses.newwin(h - 2, w - 2, y + 1, x + 1)
        rectangle(
            stdscr,
            y,
            x,
            y + h,
            x + w,
        )

        logger_win.refresh()
        return logger_win


MARGIN_LEFT, MARGIN_RIGHT, MARGIN_HEAD, MARGIN_BOTTOM = 1, 1, 1, 1


class Jap:
    def __init__(self, stdscr, text_file, options_json={}):
        self.stdscr = stdscr
        self.input_win, self.vocab_win = self.create_interface()
        self.vocab_list = self.read_vocab_file(text_file)
        self.refresh_vocab()

        self.is_repeat = options_json.get("is_repeat", False)

        scr_y, scr_x = self.vocab_win.getbegyx()
        scr_h, scr_w = self.vocab_win.getmaxyx()
        # self.logger = Logger(int(scr_h/2), int(scr_w/2), scr_y+1, int(scr_w/2), self.stdscr)

        self.stdscr.noutrefresh()
        self.input_win.noutrefresh()
        self.vocab_win.noutrefresh()

        curses.doupdate()

    def create_interface(self):
        scr_h, scr_w = self.stdscr.getmaxyx()
        input_box_x, input_box_y = MARGIN_LEFT, MARGIN_HEAD
        input_box_h, input_box_w = 4, scr_w - input_box_x - 2
        input_x, input_y, input_w, input_h = (
            input_box_x + 2,
            input_box_y + int(input_box_h / 2),
            input_box_w - 1,
            1,
        )
        input_win = curses.newwin(input_h, input_w, input_y, input_x)

        rectangle(
            self.stdscr,
            input_box_y,
            input_box_x,
            input_box_y + input_box_h,
            input_box_x + input_box_w,
        )
        vocab_box_x, vocab_box_y = input_box_x, input_box_y + input_box_h + 1
        vocab_box_w, vocab_box_y2 = input_box_w, scr_h - MARGIN_BOTTOM
        vocab_x, vocab_y, vocab_w, vocab_h = (
            vocab_box_x + 1,
            vocab_box_y + 1,
            vocab_box_w - 1,
            vocab_box_y2 - vocab_box_y - 1,
        )
        vocab_win = curses.newwin(vocab_h, vocab_w, vocab_y, vocab_x)
        rectangle(
            self.stdscr,
            vocab_box_y,
            vocab_box_x,
            vocab_box_y2,
            vocab_box_x + vocab_box_w,
        )
        self.stdscr.noutrefresh()
        vocab_win.noutrefresh()
        return input_win, vocab_win

    def pop_vocab(self):
        vocab = self.vocab_list.pop(0)
        if self.is_repeat:
            self.vocab_list.append(vocab)

    def refresh_vocab(self):
        scr_h, scr_w = self.vocab_win.getmaxyx()
        vocab_num = int(scr_h / 2)
        if len(self.vocab_list) < vocab_num:
            vocab_num = len(self.vocab_list)

        for i in range(vocab_num):
            self.vocab_win.addstr(i * 2, 1, self.vocab_list[i])
        self.vocab_win.noutrefresh()

    def read_vocab_file(self, vocab_file):
        with open(vocab_file, "r") as f:
            return f.read().splitlines()

    def write_log(self, log_string):
        with open("log.txt", "a") as f:
            f.write(f"{log_string}")

    def run(self):
        start_cursor_x = MARGIN_LEFT + 1
        vocab_label = self.vocab_list[0].split("\t")
        # self.logger.add_log(''.join(vocab_label))
        TAB = "\t"
        input_buffer = ""
        parse_mode = 1
        input_list = []
        while True:
            key = self.input_win.getch()

            # 10 is enter key
            if key == 10:
                self.input_win.erase()
                self.vocab_win.erase()
                input_buffer = ""
                self.pop_vocab()
                if not self.vocab_list:
                    curses.endwin()

                self.refresh_vocab()
                vocab_label = self.vocab_list[0].split("\t")
                parse_mode = 1
                continue
            # 127 is backspace
            elif key == 127 and input_buffer:
                if input_buffer[-1] == TAB:
                    parse_mode -= 1
                if parse_mode < 1:
                    parse_mode = 1
                input_buffer = input_buffer[:-1]
            # 23 is ctrl+w, 8 is ctrl+backspace
            elif (key == 23 or key == 8) and input_buffer:
                _buffer = input_buffer.split(TAB)[:-1]
                parse_mode = len(_buffer)
                if parse_mode == 0:
                    parse_mode = 1
                input_buffer = TAB.join(_buffer)
            # 9 is tab
            elif key == 9 and input_buffer:
                if parse_mode == 1:
                    if input_buffer == vocab_label[1]:
                        input_buffer = vocab_label[0]
                elif parse_mode == 2:
                    pass
                parse_mode += 1
                input_buffer += TAB
            elif parse_mode > 2:
                input_buffer += chr(key)
            else:
                input_buffer += chr(key)
                input_buffer = jap_parser.to_hiragana_converter(input_buffer)
            self.input_win.erase()
            self.input_win.addstr(input_buffer)
            # self.input_win.addstr(str(key))
            self.stdscr.refresh()
            curses.doupdate()
