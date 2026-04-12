# Monkey patching in Python refers to the practice of dynamically modifying or extending code at runtime typically replacing or adding new functionalities to existing modules, classes or methods without altering their original source code.
# This technique is often used for quick fixes, debugging or adding temporary features.

# Define a Class or Module to Patch
# original_module.py
class MyClass:
   def say_hello(self):
      return "Hello, Welcome to Tutorialspoint!"
# Create a Patching Function or Method
# patch_module.py
from original_module import MyClass
# Define a new function to be patched
def new_say_hello(self):
   return "Greetings!"
# Monkey patching MyClass with new_say_hello method
MyClass.say_hello = new_say_hello

# Test the Monkey Patch
# test_patch.py

from original_module import MyClass
import patch_module
# Create an instance of MyClass
obj = MyClass()
# Test the patched method
print(obj.say_hello())  # Output: Greetings!