from pynput.keyboard import Key, Controller, Listener
import time

keyboard = Controller()
flag = True

class listen(threading.Thread):
    def on_press(key):
        print('{0} pressed'.format(
            key))

    def on_release(key):
        global flag
        print('{0} release'.format(
            key))
        if key == Key.esc:
            exit()
        if key == Key.space:
            flag = False
        return False

with Listener(
    on_press=on_press, 
    on_release=on_release) as listener:
    listener.join()

class control(threading.Thread):
    def run(self, flag):
        while True:
            # if flag:
                # keyboard.press(Key.f8)
                # keyboard.release(Key.f8)
            # else:
                # keyboard.press(Key.f7)
                # keyboard.release(Key.f7)
            print(flag)
            time.sleep(1)

t1 = listen()
t2 = control()

t1.start()
t2.start()

t1.join()
t2.join()