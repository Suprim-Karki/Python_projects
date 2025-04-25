''' This checks the typing speed in WPM'''
'''pip insrall windows-curses'''

import curses
from curses import wrapper

def main(stdscr):   #stdscr = standard screen
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)    #bg and fg color
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    stdscr.clear()
    stdscr.addstr(1,0,"Hello World")   # 1,0 is the row and column 1 line down, 0 letter right
    stdscr.refresh()
    stdscr.getkey()  # prevents program from immediately closing

wrapper(main)