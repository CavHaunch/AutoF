from pynput.keyboard import Key, Controller, Listener
from time import sleep
import threading

keyboard = Controller()

global f7f8Toggle
f7f8Toggle = False
global f5flag
f5flag = False
global terminate
terminate = False
global pause
pause = True

def on_release(key):
    global f7f8Toggle
    global f5flag
    global terminate
    global pause
    print('{0} release'.format(key))
    if key == Key.esc:
        terminate = True
        return False
    if key == Key.home:
        f5flag = False
        f7f8Toggle = not f7f8Toggle
    if key == Key.end:
        f5flag = not f5flag
    if key == Key.num_lock:
        pause = not pause
        f7f8Toggle = 0
        f5flag = 0

def task():   
    global f7f8Toggle
    global f5flag
    global terminate
    global pause
    while True:
        sleep(0.5)
        if(terminate==True):
            exit()
        if(pause==False):
            if f5flag == True:
                keyboard.press(Key.f5)
                keyboard.release(Key.f5)
            else:
                if f7f8Toggle == False: 
                    keyboard.press(Key.f7)
                    keyboard.release(Key.f7)
                elif f7f8Toggle == True:
                    keyboard.press(Key.f8)
                    keyboard.release(Key.f8)
        sleep(0.5)

listener =  Listener(on_release=on_release)
t = threading.Thread(target=task)

listener.start()
t.start()
try:
    listener.join()
    t.join()
finally:
    listener.stop()