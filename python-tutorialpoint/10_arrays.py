# Index starts with 0.
# Array length is 10 which means it can store 10 elements.
# Each element can be accessed via its index. For example, we can fetch an element at index 6 as 9.

# # importing
# import array as array_name
# # creating array
# obj = array_name.array(typecode[, initializer])
# typecode − The typecode character used to speccify the type of elements in the array.
# initializer − It is an optional value from which array is initialized. It must be a list, a bytes-like object, or iterable elements of the appropriate type.

import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])
print (type(a), a)

# creating an array with char type
a = arr.array('u', 'BAT')
print (type(a), a)

# creating an array with float type
a = arr.array('d', [1.1, 2.2, 3.3])
print (type(a), a)


# Basic Operations on Python Arrays
# Following are the basic operations supported by an array −
#
# Traverse − Print all the array elements one by one.
from array import *
array1 = array('i', [10,20,30,40,50])
for x in array1:
 print(x)
# Insertion − Adds an element at the given index.
from array import *
array1 = array('i', [10,20,30,40,50])
array1.insert(1,60)
for x in array1:
 print(x)
# Deletion − Deletes an element at the given index.
from array import *
array1 = array('i', [10,20,30,40,50])
array1.remove(40)
for x in array1:
   print(x)
# Search − Searches an element using the given index or by the value.
from array import *
array1 = array('i', [10,20,30,40,50])
print (array1.index(40))
# Update − Updates an element at the given index.
from array import *
array1 = array('i', [10,20,30,40,50])
array1[2] = 80
for x in array1:
   print(x)

#  Accessing from Array
import array as arr
# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])
#indexing
print (numericArray[0])
print (numericArray[1])
print (numericArray[2])
# iteration through for loop
for item in numericArray:
   print(item)
# use of enumerate() function
for loc, val in enumerate(numericArray):
    print(f"Index: {loc}, value: {val}")
# slicing operation
print (numericArray[2:])
print (numericArray[0:3])

import array as arr
a = arr.array('i', [1, 2, 3])
a.append(10)
print (a)
a.insert(1,20)
print (a)
b = arr.array('i', [6,7,8,9,10])
a.extend(b)
print (a)

import array as arr
# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])
# before removing array
print ("Before removing:", numericArray)
# removing array
numericArray.remove(311)
# after removing array
print ("After removing:", numericArray)

# before removing array
print ("Before removing:", numericArray)
# removing array
numericArray.pop(3)
# after removing array
print ("After removing:", numericArray)

import array as arr
newArray = arr.array('i', [56, 42, 23, 85, 45])
for iterate in newArray:
   print (iterate, end=" ")

import array as arr
# creating array
a = arr.array('i', [96, 26, 56, 76, 46])
# checking the length
l = len(a)
# loop variable
idx = 0
# while loop
while idx < l:
   print (a[idx])
   # incrementing the while loop
   idx+=1

a = arr.array('d', [56, 42, 23, 85, 45])
l = len(a)
for x in range(l):
   print (a[x])

# Ways to Reverse an Array in Python
# Using slicing operation
import array as arr
# creating array
numericArray = arr.array('i', [88, 99, 77, 55, 66])
print("Original array:", numericArray)
revArray = numericArray[::-1]
print("Reversed array:",revArray)
# Using reverse() method
import array as arr
    # creating an array
numericArray = arr.array('i', [10,5,15,4,6,20,9])
print("Array before reversing:", numericArray)
    # converting the array into list
newArray = numericArray.tolist()
    # reversing the list
newArray.reverse()
    # creating a new array from reversed list
revArray = arr.array('i', newArray)
print ("Array after reversing:",revArray)
# Using reversed() method
import array as arr
    # creating an array
numericArray = arr.array('i', [12, 10, 14, 16, 20, 18])
print("Array before reversing:", numericArray)
    # reversing the array
newArray = list(reversed(numericArray))
    # creating a new array from reversed list
revArray = arr.array('i', newArray)
print ("Array after reversing:",revArray)
# Using for loop
import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i')
for i in range(len(a)-1, -1, -1):
   b.append(a[i])
print(a)
print(b)

# Bubble sort
import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
for i in range(0, len(a)):
   for j in range(i+1, len(a)):
      if(a[i] > a[j]):
         temp = a[i];
         a[i] = a[j];
         a[j] = temp;
print (a)

import array as arr
    # creating array
orgnlArray = arr.array('i', [10,5,15,4,6,20,9])
print("Original array:", orgnlArray)
    # converting to list
sortedList = orgnlArray.tolist()
    # sorting the list
sortedList.sort()
    # creating array from sorted list
sortedArray = arr.array('i', sortedList)
print("Array after sorting:",sortedArray)

import array as arr
a = arr.array('i', [4, 5, 6, 9, 10, 15, 20])
sorted(a)
print(a)

import array as arr
# creating two arrays
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])
# merging both arrays
for i in range(len(b)):
   a.append(b[i])
print (a)

import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])
x = a.tolist()
y = b.tolist()
z = x+y
a = arr.array('i', z)
print (a)

import array as arr
a = arr.array('i', [88, 99, 77, 66, 44, 22])
b = arr.array('i', [12, 17, 18, 11, 13, 10])
a.extend(b)
print (a)