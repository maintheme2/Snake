import curses
import re
import time
import keyboard
from curses import wrapper

stdscr = curses.initscr()

def boundaries_collision(y, x, cols, rows):
    stdscr.clear()
    if x < 0:
        stdscr.addstr(y, 0, "Game over")
    elif y < 0:
        stdscr.addstr(0, x, "Game over")
    elif x > cols - 1:
        stdscr.addstr(y, cols - 9, "Game over")
    elif y > rows - 1:
        stdscr.addstr(rows - 1, x, "Game over")
    stdscr.refresh()
    time.sleep(1)

def update_screen(y, x):
    stdscr.clear()
    stdscr.addstr(y, x, "-->")
    stdscr.refresh() 

def main(stdscr):

    rows, cols = stdscr.getmaxyx() # 24 80 // 34 150
    y,x = 0,0

    while True:
        key = stdscr.getkey()

        # if keyboard.is_pressed(curses.KEY_UP or "w"):
        #     while not keyboard.is_pressed(curses.KEY_DOWN or "s" 
        #     or curses.KEY_RIGHT or "d" or curses.KEY_LEFT or "a"):
        #         x += 1
        #         if x > cols - 1:
        #             boundaries_collision(y, x, cols, rows)
        #             return
        #         elif keyboard.is_pressed(curses.KEY_DOWN) or keyboard.is_pressed("s"):
        #             key = "s"
        #         elif keyboard.is_pressed(curses.KEY_LEFT) or keyboard.is_pressed("d"):
        #             key = "d"
        #         elif keyboard.is_pressed(curses.KEY_RIGHT) or keyboard.is_pressed("a"):
        #             key = "a"
        #         else:
        #             update_screen(y, x)
        #             time.sleep(0.3)

        while key in ["KEY_LEFT", "a"]:  
            x -= 1
            if x < 0:
                boundaries_collision(y, x, cols, rows)
                return
            elif keyboard.is_pressed("d") or keyboard.is_pressed(curses.KEY_RIGHT) or keyboard.is_pressed("w") or keyboard.is_pressed("s"):
                break
            else:
                update_screen(y, x)   
                time.sleep(0.3)
        while key in ["KEY_RIGHT", "d"]:
            x += 1    
            if x > cols - 1:
                boundaries_collision(y, x, cols, rows)
                return;
            elif keyboard.is_pressed("a") or keyboard.is_pressed("w") or keyboard.is_pressed("s"):
                break
            else:
                update_screen(y, x)
                time.sleep(0.3)
        while key in ["KEY_UP", "w"]:
            y -= 1
            if y < 0:
                boundaries_collision(y, x, cols, rows)
                return;
            else:
                update_screen(y, x) 
                time.sleep(0.3)
        while key in ["KEY_DOWN", "s"]:
            y += 1
            if y > rows - 1:
                boundaries_collision(y, x, cols, rows)
                return;
            else:
                update_screen(y, x) 
                time.sleep(0.3)
                

wrapper(main)            