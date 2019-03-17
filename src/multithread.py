import threading
import time

flag = True
global_lock = threading.Lock()
f = open('output.txt', 'w')

class Thr(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID

    def run(self):
        for i in range(100):
            while global_lock.locked():
                continue

            global_lock.acquire()

            with open("output.txt", "a+") as file:
                file.write("{}{}\n".format("Thread ", self.threadID))
            
            global_lock.release()
            time.sleep(0.0001)


threads = []
for i in range(1, 10):
    t = Thr(i)
    threads.append(t)
    t.start()
[thread.join() for thread in threads]