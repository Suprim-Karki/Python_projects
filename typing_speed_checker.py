''' This checks the typing speed in WPM'''
'''pip insrall windows-curses'''

import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the word typing test.")   # 1,0 is the row and column 1 line down, 0 letter right
    stdscr.addstr("\nPress enter to continue: ")   # 1,0 is the row and column 1 line down, 0 letter right
    stdscr.getkey()    # prevents program from immediately closing and stores what user typed

def display_text(stdscr,target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0,f"WPM: {wpm}")
    for i,char in enumerate(current):
        correct_char=target[i]
        color = curses.color_pair(1)
        if char!=correct_char:
            color=curses.color_pair(2)
        stdscr.addstr(0,i,char,color)
    


def wpm_test(stdscr):
    target_text="Hello World this is a test."
    current_text=[]
    wpm=0

    while True:
        stdscr.clear()
        display_text(stdscr,target_text,current_text,wpm)
        stdscr.refresh() 
        key = stdscr.getkey()
        if ord(key)==27:
            break
        if key in ("KEY_BACKSPACE","\b","\x7f"):
            if len(current_text)>0:
                current_text.pop()
        elif len(current_text)<len(target_text):
            current_text.append(key)

def main(stdscr):   #stdscr = standard screen
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)    #bg and fg color
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)