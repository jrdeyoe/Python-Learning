import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    GREEN_BLACK = curses.color_pair(1)
    BLUE_BLACK = curses.color_pair(2)
    
    stdscr.clear()
   
    for i in range(70):
        stdscr.clear()
        color = BLUE_BLACK

        if i % 2 == 0:
            color = GREEN_BLACK
        
        stdscr.addstr(10, 35, f"IT'S PARTY TIME!!!!", color | curses.A_BOLD)
        stdscr.refresh()
        time.sleep(0.1)

    stdscr.addstr(12,37, "PARTY IS OVER!!!!", curses.A_UNDERLINE)
    stdscr.refresh()
    time.sleep(2)
    stdscr.addstr(14,39, "TIME TO GO HOME!", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getch()

wrapper(main)