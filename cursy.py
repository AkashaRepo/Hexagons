import curses
from curses import wrapper

def main(stdscr):
    curses.noecho()
    myscreen = curses.initscr()
    myscreen.addstr(3, 6, "Press any key to continue!")
    myscreen.refresh()
    ch = chr(myscreen.getch())
    myscreen.addstr(4, 6, 'you pressed the "%s" key!' %(ch))
    myscreen.refresh()
    myscreen.getch()
    curses.endwin()

wrapper(main)
