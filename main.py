import curses
import sys
import threading
import time
from datetime import datetime

import keyboard
import pytz

TGREEN = '\033[32m'  # Green Text


def print_time():
    while True:
        if keyboard.is_pressed('q'):
            sys.exit()
        UTC = pytz.utc
        Asia = pytz.timezone('Asia/Shanghai')
        New_York = pytz.timezone('America/New_York')
        Moscow = pytz.timezone('Europe/Moscow')
        London = pytz.timezone('Europe/London')

        Asia = datetime.now(Asia)
        New_York = datetime.now(New_York)
        Moscow = datetime.now(Moscow)
        London = datetime.now(London)

        New_York = str(New_York)
        London = str(London)
        Moscow = str(Moscow)
        Asia = str(Asia)

        screen = curses.initscr()
        curses.start_color()
        curses.use_default_colors()

        # Update the buffer, adding text at different locations
        screen.addstr(1, 1,  "London:", curses.color_pair(2))
        screen.addstr(1, 15, London, curses.color_pair(4))
        screen.addstr(5, 1, "Moscow:", curses.color_pair(2))
        screen.addstr(5, 15, Moscow, curses.color_pair(4))
        screen.addstr(10, 1, "New York:", curses.color_pair(2))
        screen.addstr(10, 15, New_York, curses.color_pair(4))
        screen.addstr(15, 1, "Shanghai:", curses.color_pair(2))
        screen.addstr(15, 15, Asia, curses.color_pair(4))
        # Changes go in to the screen buffer and only get
        # displayed after calling `refresh()` to update
        screen.refresh()


t1 = threading.Thread(target=print_time)

# starting thread 1
t1.start()
# starting thread 2
