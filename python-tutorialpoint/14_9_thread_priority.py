# Setting the Thread Priority Using Sleep()
import threading
import time
class DummyThread(threading.Thread):
   def __init__(self, name, priority):
      threading.Thread.__init__(self)
      self.name = name
      self.priority = priority
   def run(self):
      name = self.name
      time.sleep(1.0 * self.priority)
      print(f"{name} thread with priority {self.priority} is running")
# Creating threads with different priorities
t1 = DummyThread(name='Thread-1', priority=4)
t2 = DummyThread(name='Thread-2', priority=1)
# Starting the threads
t1.start()
t2.start()
# Waiting for both threads to complete
t1.join()
t2.join()
print('All Threads are executed')

# Prioritizing Python Threads Using the Queue Module
from time import sleep
from random import random, randint
from threading import Thread
from queue import PriorityQueue

queue = PriorityQueue()

def producer(queue):
   print('Producer: Running')
   for i in range(5):
      # create item with priority
      value = random()
      priority = randint(0, 5)
      item = (priority, value)
      queue.put(item)
   # wait for all items to be processed
   queue.join()
   queue.put(None)
   print('Producer: Done')

def consumer(queue):
   print('Consumer: Running')
   while True:
      # get a unit of work
      item = queue.get()
      if item is None:
         break
      sleep(item[1])
      print(item)
      queue.task_done()
   print('Consumer: Done')
producer = Thread(target=producer, args=(queue,))
producer.start()
consumer = Thread(target=consumer, args=(queue,))
consumer.start()
producer.join()
consumer.join()