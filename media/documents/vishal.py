import threading
import time

def loop1_10():
    for i in range(1, 5):
        time.sleep(1)
        print(i)

def loop1():
    for i in range(1, 5):
        time.sleep(1)
        print(i)

threading.Thread(target=loop1_10).start()
threading.Thread(target=loop1).start()
