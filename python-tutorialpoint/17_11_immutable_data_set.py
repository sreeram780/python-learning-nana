empty_tuple = ()
single_element_tuple = (5,)  # Note the comma after the single element
print("Single element tuple:", single_element_tuple)
multi_element_tuple = (1, 2, 'Tutorialspoint', 3.14)
print("Multi elements tuple:", multi_element_tuple)
nested_tuple = (1, (2, 3), 'Learning')
print("Nested tuple:", nested_tuple)

# Understanding Tuple Immutability in Python
# Define a tuple
my_tuple = (1, 2, 3, 'hello')
# Attempt to modify an element (which is not possible with tuples)
# This will raise a TypeError
try:
   my_tuple[0] = 10
except TypeError as e:
   print(f"Error: {e}")
# Even trying to append or extend a tuple will result in an error
try:
   my_tuple.append(4)
except AttributeError as e:
   print(f"Error: {e}")
# Trying to reassign the entire tuple to a new value is also not allowed
try:
   my_tuple = (4, 5, 6)
except TypeError as e:
   print(f"Error: {e}")
print("Original tuple:", my_tuple)


# Example demonstrating string immutability
my_string = "Hello"

# Attempting to modify a string will create a new string instead of modifying the original
modified_string = my_string + " Learners"
print(modified_string)  # Output: Hello Learners

# Original string remains unchanged
print(my_string)  # Output: Hello

# Trying to modify the string directly will raise an error
try:
   my_string[0] = 'h'  # TypeError: 'str' object does not support item assignment
except TypeError as e:
   print(f"Error: {e}")


# Creating a frozenset
frozen_set = frozenset([1, 2, 3, 4])
# Attempting to add an element to the frozenset will raise an error
try:
   frozen_set.add(5)
except AttributeError as e:
   print(f"Error: {e}")
# Attempting to remove an element from the frozenset will also raise an error
try:
   frozen_set.remove(2)
except AttributeError as e:
   print(f"Error: {e}")
# The original frozenset remains unchanged
print("Original frozenset:", frozen_set)

# Understanding Named Tuples Immutability in Python

from collections import namedtuple
# Define a named tuple called Point with fields 'x' and 'y'
Point = namedtuple('Point', ['x', 'y'])
# Create an instance of Point
p = Point(x=1, y=2)
print(p)
# Attempt to modify the named tuple
# This will raise an AttributeError since named tuples are immutable
try:
   p.x = 10
except AttributeError as e:
   print(f"Error occurred: {e}")
# Accessing elements in a named tuple is similar to accessing elements in a regular tuple
print(p.x)
print(p.y)