my_set = {1, 2, 3, 4, 5}
print (my_set)

my_set = set([1, 2, 3, 4, 5])
print (my_set)

# Duplicate Elements in Set
my_set = {1, 2, 2, 3, 3, 4, 5, 5}
print (my_set)

mixed_set = {1, 'hello', (1, 2, 3)}
print (mixed_set)

my_set = {1, 2, 3, 3}
# Adding an element 4 to the set
my_set.add(4)
print (my_set)

my_set = {1, 2, 3, 4}
# Removes the element 3 from the set
my_set.remove(3)
print (my_set)

# discard
my_set = {1, 2, 3, 4}
# No error even if 5 is not in the set
my_set.discard(5)
print (my_set)

my_set = {1, 2, 3, 4}
if 2 in my_set:
   print("2 is present in the set")
else:
   print("2 is not present in the set")

even_set = {x for x in range(1, 11) if x % 2 == 0}
print(even_set)

# frozenset
# my_frozen_set = frozenset([1, 2, 3])
# print(my_frozen_set)
# my_frozen_set.add(4)

# Defining a set
langs = {"C", "C++", "Java", "Python"}
# Accessing set items using a for loop
for lang in langs:
   print (lang)

# Checking if an item exists in the set
if "Java" in langs:
    print("Java is present in the set.")
else:
    print("Java is not present in the set.")

# Checking if an item does not exist in the set
if "SQL" not in langs:
    print("SQL is not present in the set.")
else:
    print("SQL is present in the set.")

# Defining a list containing integers
numbers = [1, 2, 3, 4, 5]
# Creating a set containing squares of numbers using set comprehension
squares_set = {num ** 2 for num in numbers}
# Printing the set containing squares of numbers
print("Squares Set:", squares_set)

my_set = {"Rohan", "Physics", 21, 69.75}
print ("Original set: ", my_set)
my_set.remove("Physics")
print ("Set after removing: ", my_set)

# Defining a set
my_set = {1, 2, 3, 4, 5}
# removing and returning an arbitrary element from the set
removed_element = my_set.pop()
# Printing the removed element and the updated set
print("Removed Element:", removed_element)
print("Updated Set:", my_set)

# Defining a set with multiple elements
my_set = {1, 2, 3, 4, 5}
# Removing all elements from the set
my_set.clear()
# Printing the updated set
print("Updated Set:", my_set)

s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = s1|s2
print (s3)

s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = s1.union(s2)
print (s3)

s1={1,2,3,4,5}
s2={4,5,6,7,8}
s1.update(s2)
print (s1)

# Set Operations
# These methods perform set operations such as union, intersection, difference, and symmetric difference −
#
# Sr.No.	Methods with Description
# 1
# set.update()
#
# Update a set with the union of itself and others.
#
# 2
# set.difference_update()
#
# Remove all elements of another set from this set.
#
# 3
# set.intersection()
#
# Returns the intersection of two sets as a new set.
#
# 4
# set.intersection_update()
#
# Updates a set with the intersection of itself and another.
#
# 5
# set.isdisjoint()
#
# Returns True if two sets have a null intersection.
#
# 6
# set.issubset()
#
# Returns True if another set contains this set.
#
# 7
# set.issuperset()
#
# Returns True if this set contains another set.
#
# 8
# set.symmetric_difference()
#
# Returns the symmetric difference of two sets as a new set.
#
# 9
# set.symmetric_difference_update()
#
# Update a set with the symmetric difference of itself and another.
#
# 10
# set.union()

Returns the union of sets as a new set.

11
set.difference()

Returns the difference of two or more sets as a new set.