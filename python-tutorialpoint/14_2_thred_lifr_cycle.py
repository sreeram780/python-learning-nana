# States of a Thread Life Cycle in Python
#   Creating a Thread − To create a new thread in Python, you typically use the Thread class from the threading module.
#   Starting a Thread − Once a thread object is created, it must be started by calling its start() method. This initiates the thread's activity and invokes its run() method in a separate thread.
#   Paused/Blocked State − Threads can be paused or blocked for various reasons, such as waiting for I/O operations to complete or another thread to perform a task. This is typically managed by calling its join() method. This blocks the calling thread until the thread being joined terminates.
#   Synchronizing Threads − Synchronization ensures orderly execution and shared resource management among threads. This can be done by using synchronization primitives like locks, semaphores, or condition variables.
#   Termination − A thread terminates when its run() method completes execution, either by finishing its task or encountering an exception.

#  example-1

import threading
def func(x):
   print('Current Thread Details:', threading.current_thread())
   for n in range(x):
      print('{} Running'.format(threading.current_thread().name), n)
   print('Internal Thread Finished...')
# Create thread objects
t1 = threading.Thread(target=func, args=(2,))
t2 = threading.Thread(target=func, args=(3,))
# Start the threads
print('Thread State: CREATED')
t1.start()
t2.start()
# Wait for threads to complete
t1.join()
t2.join()
print('Threads State: FINISHED')
# Simulate main thread work
for i in range(3):
   print('Main Thread Running', i)
print("Main Thread Finished...")

#  example 2
import threading
import time

# Create a semaphore
semaphore = threading.Semaphore(2)

def worker():
   with semaphore:
      print('{} has started working'.format(threading.current_thread().name))
      time.sleep(2)
      print('{} has finished working'.format(threading.current_thread().name))
# Create a list to keep track of thread objects
threads = []
# Create and start 5 threads
for i in range(5):
   t = threading.Thread(target=worker, name='Thread-{}'.format(i+1))
   threads.append(t)
   print('{} has been created'.format(t.name))
   t.start()
# Wait for all threads to complete
for t in threads:
   t.join()
   print('{} has terminated'.format(t.name))
print('Threads State: All are FINISHED')
print("Main Thread Finished...")