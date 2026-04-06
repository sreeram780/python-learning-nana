# Creating a thread using the threading module is generally recommended due to its higher-level interface and additional functionalities.
# On the other hand, the _thread module offers a simpler, lower-level approach to create and manage threads, which can be useful for straightforward, low-overhead threading tasks.

# Creating Threads with Functions
from threading import Thread
def addition_of_numbers(x, y):
   result = x + y
   print('Addition of {} + {} = {}'.format(x, y, result))
def cube_number(i):
   result = i ** 3
   print('Cube of {} = {}'.format(i, result))
def basic_function():
   print("Basic function is running concurrently...")
Thread(target=addition_of_numbers, args=(2, 4)).start()
Thread(target=cube_number, args=(4,)).start()
Thread(target=basic_function).start()

#  Creating Threads by Extending the Thread Class
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, 5, self.counter)
      print ("Exiting " + self.name)
def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1
# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
# Start new Threads
thread1.start()
thread2.start()
print ("Exiting Main Thread")

# Creating Threads using start_new_thread() Function

import _thread
import time


# Define a function for the thread
def thread_task(threadName, delay):
    for count in range(1, 6):
        time.sleep(delay)
        print("Thread name: {} Count: {}".format(threadName, count))


# Create two threads as follows
try:
    _thread.start_new_thread(thread_task, ("Thread-1", 2,))
    _thread.start_new_thread(thread_task, ("Thread-2", 4,))
except:
    print("Error: unable to start thread")

while True:
    pass

thread_task("test", 0.3)