# Original tuple
T1 = (10, 20, 30, 40)
# Convert tuple to list
list_T1 = list(T1)
# Elements to be added
new_elements = [50, 60, 70]
# Updating the list using append()
for element in new_elements:
    list_T1.append(element)
# Converting list back to tuple
updated_tuple = tuple(list_T1)
# Printing the updated tuple
print("Original Tuple:", T1)
print("Updated Tuple:", updated_tuple)

tup1 = (10,20,30, 40, 50, 60)
*x, y, z = tup1
print ("x: ",x, "y: ", y, "z: ", z)

# loop through tuple
tup = (25, 12, 10, -21, 10, 100)
for num in tup:
   print (num, end = ' ')

my_tup = (1, 2, 3, 4, 5)
index = 0

while index < len(my_tup):
   print(my_tup[index])
   index += 1

# Two tuples to be joined
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
# Joining the tuples
joined_tuple = T1 + T2

# Printing the joined tuple
print("Joined Tuple:", joined_tuple)

# Two tuples to be joined
T1 = (36, 24, 3)
T2 = (84, 5, 81)
# Joining the tuples using list comprehension
joined_tuple = [item for subtuple in [T1, T2] for item in subtuple]
# Printing the joined tuple
print("Joined Tuple:", joined_tuple)

from collections import namedtuple
# Define a namedtuple
Point = namedtuple('typename', fieldnames)
# Type Name: The typename is the name of the namedtuple class. It is a string that represents the name of the tuple type.
# Field Names: The field names are the names of the elements in the tuple. They are defined as a list of strings.