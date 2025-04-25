''' This checks the typing speed in WPM'''
'''pip insrall windows-curses'''

import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the word typing test.")   # 1,0 is the row and column 1 line down, 0 letter right
    stdscr.addstr("\nPress enter to continue: ")   # 1,0 is the row and column 1 line down, 0 letter right
    stdscr.getkey()    # prevents program from immediately closing and stores what user typed

def wpm_test(stdscr):
    target_text="Hello World this is a test."
    current_text=[]

    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()

    while True:
        key = stdscr.getkey()
        current_text.append(key)
        for char in current_text:
            stdscr.addstr(char,curses.color_pair(1))
        stdscr.refresh()

def main(stdscr):   #stdscr = standard screen
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)    #bg and fg color
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)