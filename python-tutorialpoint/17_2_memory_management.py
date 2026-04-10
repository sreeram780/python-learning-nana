
import sys

# Create a string object
name = "Tutorialspoint"
print("Initial reference count:", sys.getrefcount(name))
# Assign the same string to another variable
other_name = "Tutorialspoint"
print("Reference count after assignment:", sys.getrefcount(name))
# Concatenate the string with another string
string_sum = name + ' Python'
print("Reference count after concatenation:", sys.getrefcount(name))
# Put the name inside a list multiple times
list_of_names = [name, name, name]
print("Reference count after creating a list with 'name' 3 times:", sys.getrefcount(name))
# Deleting one more reference to 'name'
del other_name
print("Reference count after deleting 'other_name':", sys.getrefcount(name))
# Deleting the list reference
del list_of_names
print("Reference count after deleting the list:", sys.getrefcount(name))