# import threading
# import time
# import random

# buffer = []
# bufsize = 5

# def producer():
#     for i in range(10):
#         if len(buffer) == bufsize:
#             print("Buffer full. Producer waits.")
#         else:
#             buffer.append(i)
#             print(f"Produced: {i}")
#         time.sleep(random.random())

# def consumer():
#     for i in range(10):
#         if len(buffer) == 0:
#             print("Buffer empty. Consumer waits.")
#         else:
#             item = buffer.pop(0)
#             print(f"Consumed: {item}")
#         time.sleep(random.random())

# t1 = threading.Thread(target=producer)
# t2 = threading.Thread(target=consumer)

# t1.start()
# t2.start()

# t1.join()
# t2.join()


from threading import Thread, Semaphore, Lock
import time, random

buffer = []
bufsize = 5

empty = Semaphore(bufsize)  # available slots
full = Semaphore(0)         # filled slots
mutex = Lock()              # buffer access lock

def producer():
    for i in range(10):
        empty.acquire()
        mutex.acquire()
        buffer.append(i)
        print(f"Produced: {i}")
        mutex.release()
        full.release()
        time.sleep(random.random())

def consumer():
    for i in range(10):
        full.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        print(f"Consumed: {item}")
        mutex.release()
        empty.release()
        time.sleep(random.random())

t1 = Thread(target=producer)
t2 = Thread(target=consumer)

t1.start()
t2.start()
t1.join()
t2.join()
