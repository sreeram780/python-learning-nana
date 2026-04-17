class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

with MyContextManager():
    print("body")

class MyContextManager:
   def __enter__(self):
      print("Entering the context")
      return self
   def __exit__(self, exc_type, exc_value, traceback):
      print("Exiting the context")
      if exc_type:
         print("An exception occurred")
      return True  # Suppress exception

with MyContextManager():
   print("body")
   name =  "Python"/3 #to raise an exception

import asyncio
class AsyncContextManager:
   async def __aenter__(self):
      print("Entering the async context class")
      return self
   async def __aexit__(self, exc_type, exc_value, traceback):
      print("Exiting the async context class")
      if exc_type:
         print("Exception occurred")
      return True
async def main():
   async with AsyncContextManager():
      print("Inside the async context")
      name =  "Python"/3 #to raise an exception

asyncio.run(main())

# Creating Custom Context Managers
from contextlib import contextmanager
@contextmanager
def my_context_manager():
   print("Entering the context manager method")
   try:
      yield
   finally:
      print("Exiting the context manager method")
with my_context_manager():
   print("Inside the context")

# Using the contextlib.asynccontextmanager() Function
import asyncio
from contextlib import asynccontextmanager
@asynccontextmanager
async def async_context_manager():
   try:
      print("Entering the async context")
      # Perform async setup tasks if needed
      yield
   finally:
      # Perform async cleanup tasks if needed
      print("Exiting the async context")
async def main():
   async with async_context_manager():
      print("Inside the async context")
      await asyncio.sleep(1)  # Simulating an async operation

# Run the asyncio event loop
asyncio.run(main())