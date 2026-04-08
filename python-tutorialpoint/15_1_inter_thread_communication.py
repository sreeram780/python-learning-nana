from threading import Event, Thread
import time
terminate = False
def signal_state():
    global terminate
    while not terminate:
        time.sleep(0.5)
        print("Traffic Police Giving GREEN Signal")
        event.set()
        time.sleep(1)
        print("Traffic Police Giving RED Signal")
        event.clear()
def traffic_flow():
    global terminate
    num = 0
    while num < 10 and not terminate:
        print("Waiting for GREEN Signal")
        event.wait()
        print("GREEN Signal ... Traffic can move")
        while event.is_set() and not terminate:
            num += 1
            print("Vehicle No:", num," Crossing the Signal")
            time.sleep(1)
        print("RED Signal ... Traffic has to wait")
event = Event()
t1 = Thread(target=signal_state)
t2 = Thread(target=traffic_flow)
t1.start()
t2.start()
# Terminate the threads after some time
time.sleep(5)
terminate = True
# join all threads to complete
t1.join()
t2.join()
print("Exiting Main Thread")

# The Condition Object
from threading import Condition, Thread
import time
c = Condition()
def thread_a():
    print("Thread A started")
    with c:
        print("Thread A waiting for permission...")
        c.wait()
        print("Thread A got permission!")
    print("Thread A finished")
def thread_b():
    print("Thread B started")
    with c:
        time.sleep(2)
        print("Notifying Thread A...")
        c.notify()
    print("Thread B finished")
Thread(target=thread_a).start()
Thread(target=thread_b).start()


# example
from threading import Condition, Thread
import time
import random
numbers = []
def taskA(c):
    for _ in range(5):
        with c:
            num = random.randint(1, 10)
            print("Generated random number:", num)
            numbers.append(num)
            print("Notification issued")
            c.notify()
        time.sleep(0.3)
def taskB(c):
    for i in range(5):
        with c:
            print("waiting for update")
            while not numbers:
                c.wait()
            print("Obtained random number", numbers.pop())
        time.sleep(0.3)
c = Condition()
t1 = Thread(target=taskB, args=(c,))
t2 = Thread(target=taskA, args=(c,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Done")