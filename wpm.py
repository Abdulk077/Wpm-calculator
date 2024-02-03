import curses
# first install the curses by Pip install curses
# for color in interface
from curses import wrapper
import time
import random



def start_screen(stdscr):
    # this funtion we create to shoe or welcome screen here  welcome to our user by some text presentation
    stdscr.clear()
    stdscr.addstr( "Welcome to Speed Typing Test! ")
    stdscr.addstr("\n Press any key to begin! ")
    stdscr.refresh()
    stdscr.getkey()
def display_text(stdscr, target, current,wpm=0):
    # This funtion we used for the Show our text with which we test user is grong or write pair one for correct typing and pair two for grong typing
    stdscr.addstr(target)
    stdscr.addstr(1,0, f"WPM is : {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)

def load_text():
    # Here in this funtion we have  the text for testing
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def wpm_test(stdscr):
    # Here we Write the program to calcualte the typing speed of the user
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round( (len(current_text) / (time_elapsed / 60)) / 5)
        stdscr.clear()
        display_text(stdscr,target_text,current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue
        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

def main(stdscr):
    # Here we create this funtion to controll and here we make our color for the text by using curses library
    # Pair one for  the correct typing it override green color with text
    # Painr two indicate the wrong typing
    # Pair three for represent the text in white color
    curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE, curses.COLOR_BLACK)
    # first we initialize foreground colour then background color

    start_screen(stdscr)
    # this while loop have controll of our all function
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2,0,"you complete the text ! press any key to continue... ")
        key = stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main)