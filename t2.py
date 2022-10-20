import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    GREEN_BLACK = curses.color_pair(1)
    RED_BLACK = curses.color_pair(2)

    pad = curses.newpad(100,100)
    stdscr.refresh()

    stdscr.addstr(4,5, "> Loading hax0r tools...")
    stdscr.refresh()
    time.sleep(2)
    stdscr.addstr(5,5, "> Obtaining IP from Google...")
    stdscr.refresh()
    time.sleep(2)
    stdscr.addstr(6,5, "> Downloading more RAM...")
    stdscr.refresh()
    time.sleep(2)
    
    stdscr.addstr(4,5,"!!! Hacking In Progress...")
    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            char = chr(67 + j)
            pad.addstr(char, GREEN_BLACK)

    for i in range(50):
        pad.refresh(0,i,5,5,30,80)
        stdscr.addstr(4,28, "."*i)
        stdscr.refresh()
        time.sleep(0.1)
    
    stdscr.addstr(14,32, "[U GOT HACKED!]", RED_BLACK | curses.A_BOLD)
    stdscr.refresh()
    time.sleep(1)
    stdscr.addstr(18,32, "[  OH  NOES!  ]", RED_BLACK | curses.A_BOLD)
    stdscr.getch()

wrapper(main)