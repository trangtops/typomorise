from asyncio.log import logger
import curses
from curses.textpad import rectangle
import jap_parser
import thai_parser


MARGIN_LEFT, MARGIN_RIGHT, MARGIN_HEAD, MARGIN_BOTTOM = 1, 1, 1, 1


class Jap:
    def __init__(self, stdscr, vocab_list, options_json={}):
        self.stdscr = stdscr
        self.splitter = "/"
        self.TAB = "\t"
        self.vocab_list = []
        self.is_test = options_json.get("is_test", False)
        self.is_shuffle = options_json.get("is_shuffle", False)
        self.input_win, self.vocab_win = self.create_interface()
        self.load_vocab_list(vocab_list)
        self.is_kanji = True
        self.is_yomi = True
        self.is_meaning = True
        self.correct_ans = []
        self.wrong_ans = []
        self.refresh_vocab()

        self.is_repeat = options_json.get("is_repeat", False)

        scr_y, scr_x = self.vocab_win.getbegyx()
        scr_h, scr_w = self.vocab_win.getmaxyx()
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

    def pop_vocab(self, ans):
        kanji = ans.split(self.TAB)[0]
        vocab = self.vocab_list.pop(0)
        if self.is_test:
            if kanji != vocab.split(self.splitter)[0]:
                self.wrong_ans.append(vocab)
            else:
                self.correct_ans.append(vocab)

        if self.is_repeat:
            self.vocab_list.append(vocab)

    def refresh_vocab(self):
        scr_h, scr_w = self.vocab_win.getmaxyx()
        self.vocab_win.erase()
        vocab_num = int(scr_h / 2)
        if len(self.vocab_list) < vocab_num:
            vocab_num = len(self.vocab_list)

        for i in range(vocab_num):
            vocab = self.vocab_list[i].split(self.splitter)
            kanji = vocab[0] if self.is_kanji else ""
            meaning = vocab[-1] if self.is_meaning else ""
            if len(vocab) == 2:
                yomi = ""
            else:
                yomi = vocab[1] if self.is_yomi else ""
            vocab = "{:<10}{:<10}{:>10}".format(kanji, meaning, yomi)
            self.vocab_win.addstr(i * 2, 1, vocab)
            self.vocab_win.noutrefresh()

    def load_vocab_list(self, vocab_list):
        # remove invalid vocab
        self.vocab_list = vocab_list
        for i in range(len(self.vocab_list)):
            vocab = self.vocab_list[i]
            vocab.replace(" ", "").replace("\t", "")
            if not vocab:
                self.vocab_list.pop(i)
        if self.is_shuffle:
            import random

            random.shuffle(self.vocab_list)

    def write_log(self, log_string):
        with open("log.txt", "a") as f:
            f.write(log_string)

    def run(self):
        start_cursor_x = MARGIN_LEFT + 1
        vocab_label = self.vocab_list[0].split(self.splitter)
        # self.logger.add_log(''.join(vocab_label))
        self.TAB = "\t"
        input_buffer = ""
        parse_mode = 1
        input_list = []
        while True:
            key = self.input_win.getch()

            # 10 is enter key
            if key == 10:
                self.input_win.erase()
                self.vocab_win.erase()
                self.pop_vocab(input_buffer)
                input_buffer = ""
                if len(self.vocab_list) == 0:
                    break
                self.refresh_vocab()
                vocab_label = self.vocab_list[0].split(self.splitter)
                parse_mode = 1
                continue
            # 127 is backspace
            elif key == 127:
                if not input_buffer:
                    continue
                if input_buffer[-1] == self.TAB:
                    parse_mode -= 1
                if parse_mode < 1:
                    parse_mode = 1
                input_buffer = input_buffer[:-1]
            # 23 is ctrl+w, 8 is ctrl+backspace
            elif key == 8:
                if not input_buffer:
                    continue
                input_list = input_buffer.split(self.TAB)
                _buffer = input_list[:-1]
                parse_mode = len(_buffer)
                input_buffer = self.TAB.join(_buffer)
                if parse_mode > 0 and input_list[-1]:
                    input_buffer += self.TAB
                    parse_mode += 1
                if parse_mode == 0:
                    parse_mode = 1
            # 9 is tab
            elif key == 9 and input_buffer:
                if parse_mode == 1:
                    if input_buffer == vocab_label[1]:
                        input_buffer = vocab_label[0]
                elif parse_mode == 2:
                    pass
                parse_mode += 1
                input_buffer += self.TAB
            # 23 is ctrl+w
            elif key == 23:
                self.is_kanji = False if self.is_kanji else True
                self.refresh_vocab()
            # 5 is ctrl+e
            elif key == 5:
                self.is_yomi = False if self.is_yomi else True
                self.refresh_vocab()
            # 18 os ctrl+r
            elif key == 18:
                self.is_meaning = False if self.is_meaning else True
                self.refresh_vocab()
            elif parse_mode > 1:
                """if ord(vocab_label[-1][0]) not in range(65, 123):
                    input_buffer += thai_parser.to_thai(chr(key))
                else:"""
                input_buffer += chr(key)
            else:
                input_buffer += chr(key)
                input_buffer = jap_parser.to_hiragana_converter(input_buffer)
            self.input_win.erase()
            self.input_win.addstr(input_buffer)
            # self.input_win.addstr(str(key))
            curses.doupdate()
