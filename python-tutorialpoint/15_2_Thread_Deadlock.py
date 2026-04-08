
from threading import Thread, Lock
import time

lock=Lock()
threads=[]

class myThread(Thread):
   def __init__(self,name):
      Thread.__init__(self)
      self.name=name
   def run(self):
      lock.acquire()
      synchronized(self.name)
      lock.release()
def synchronized(threadName):
   print ("{} has acquired lock and is running synchronized method".format(threadName))
   counter=5
   while counter:
      print ('**', end='')
      time.sleep(2)
      counter=counter-1
   print('\nlock released for', threadName)
t1=myThread('Thread1')
t2=myThread('Thread2')
t1.start()
threads.append(t1)
t2.start()
threads.append(t2)
for t in threads:
   t.join()
print ("end of main thread")


from threading import *
import time
# creating thread instance where count = 3
lock = Semaphore(4)
# creating instance
def synchronized(name):
    # calling acquire method
    lock.acquire()
    for n in range(3):
        print('Hello! ', end='')
        time.sleep(1)
        print(name)
        # calling release method
        lock.release()
# creating multiple thread
thread_1 = Thread(target=synchronized, args=('Thread 1',))
thread_2 = Thread(target=synchronized, args=('Thread 2',))
thread_3 = Thread(target=synchronized, args=('Thread 3',))
# calling the threads
thread_1.start()
thread_2.start()
thread_3.start()