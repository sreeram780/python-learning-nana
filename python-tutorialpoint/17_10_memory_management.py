# 1. Unreleased References
def create_list():
   my_list = [1] * (10**6)
   return my_list
my_list = create_list()
# If my_list is not cleared or reassigned, it continues to consume memory.
print(my_list)

# 2. Circular References
class Node:
   def __init__(self, value):
      self.value = value
      self.next = None
a = Node(1)
b = Node(2)
a.next = b
b.next = a

# 3. Global Variables
large_data = [1] * (10**6)
def process_data():
   global large_data
   # Use large_data
   pass
# large_data remains in memory as long as the program runs.

# 4. Long-Lived Objects
cache = {}
def cache_data(key, value):
   cache[key] = value
   # Cached data remains in memory until explicitly cleared.

# 5. Improper Use of Closures
def create_closure():
   large_object = [1] * (10**6)
   def closure():
      return large_object
   return closure
my_closure = create_closure()
# The large_object is retained by the closure, causing a memory leak.

# Tools for Diagnosing Memory Leaks
# 1. Using the "gc" Module
import gc
# Enable automatic garbage collection
gc.enable()
# Collect garbage and return unreachable objects
unreachable_objects = gc.collect()
print(f"Unreachable objects: {unreachable_objects}")
# Get a list of all objects tracked by the garbage collector
all_objects = gc.get_objects()
print(f"Number of tracked objects: {len(all_objects)}")