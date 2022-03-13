import curses


def make_me_an_error(screen, numerator, denominator):
    print("dssdddddd")
    screen.addstr(0, 0, str(numerator / denominator))  # divide by zero


curses.wrapper(make_me_an_error, 1, 0)
