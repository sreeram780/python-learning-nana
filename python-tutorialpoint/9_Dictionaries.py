
d1 = {"Banana":"Fruit", "Rose":"Flower", "Lotus":"Flower", "Mango":"Fruit"}
d2 = {"Fruit":"Banana","Flower":"Rose", "Fruit":"Mango", "Flower":"Lotus"}
print (d1)
print (d2)

# Creating a dictionary using curly braces
sports_player = {
   "Name": "Sachin Tendulkar",
   "Age": 48,
   "Sport": "Cricket"
}
print ("Dictionary using curly braces:", sports_player)
# Creating a dictionary using the dict() function
student_info = dict(name="Alice", age=21, major="Computer Science")
print("Dictionary using dict():",student_info)

student_info = {
   "name": "Alice",
   "age": 22,
   "major": "Computer Science",
   "graduation_year": 2023
}
# Removing an item using the del statement
del student_info["major"]
# Removing an item using the pop() method
graduation_year = student_info.pop("graduation_year")
print(student_info)

student_info = {
   "name": "Alice",
   "age": 22,
   "major": "Computer Science",
   "graduation_year": 2023
}
# Iterating through keys
for key in student_info:
   print("Keys:",key, student_info[key])
# Iterating through values
for value in student_info.values():
   print("Values:",value)
# Iterating through key-value pairs
for key, value in student_info.items():
   print("Key:Value:",key, value)

# Using square brackets []
# The get() method
# Iterating through the dictionary using loops
# Or specific methods like keys(), values(), and items()

capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Gujarat is: ", capitals.get('Gujarat'))
print ("Capital of Karnataka is: ", capitals.get('Karnataka'))

# Creating a dictionary with keys and values
student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}
# Accessing all keys using the keys() method
all_keys = student_info.keys()
print("Keys:", all_keys)

# Creating a dictionary with student information
student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}
# Accessing dictionary values using the get() method
major = student_info.get("major")
# Default value provided if key is not found
grad_year = student_info.get("graduation_year", "2023")

print("Major:", major)
print("Graduation Year:", grad_year)

# Creating a dictionary with keys and values
student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}
# Accessing all values using the values() method
all_values = student_info.values()
print("Values:", all_values)

# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Modifying the value associated with the key 'age'
person['age'] = 26
print(person)

# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Updating multiple values
person.update({'age': 26, 'city': 'Los Angeles'})
print(person)

# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Conditionally modifying the value associated with 'age'
if person['age'] == 25:
   person['age'] = 26
print(person)

# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Removing the key-value pair associated with the key 'age'
removed_age = person.pop('age')

print(person)
print("Removed age:", removed_age)

# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Removing the last key-value pair
removed_item = person.popitem()

print(person)
print("Removed item:", removed_item)

# We can add dictionary items in Python using various ways such as −
#
# Using square brackets
# Using the update() method
marks = {"Savita":67, "Imtiaz":88}
print ("Initial dictionary: ", marks)
marks.update({'Kavya': 58, 'Mohan': 98})
print ("Dictionary after new addition: ", marks)
# Using a comprehension
# Using unpacking
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
newmarks = {**marks, **marks1}
print ("marks dictionary after update: \n", newmarks)
# Using the Union Operator
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
newmarks = marks | marks1
print ("marks dictionary after update: \n", newmarks)
# Using the |= Operator
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
marks |= marks1
print ("marks dictionary after update: \n", marks)
# Using setdefault() method
# Initial dictionary
student = {"name": "Alice", "age": 21}
# Adding a new key-value pair
major = student.setdefault("major", "Computer Science")
print(student)
# Using collections.defaultdict() method
from collections import defaultdict
# Using int as the default factory to initialize missing keys with 0
d = defaultdict(int)
# Incrementing the value for key 'a'
d["a"] += 1
print(d)

# Using list as the default factory to initialize missing keys with an empty list
d = defaultdict(list)
# Appending to the list for key 'b'
d["b"].append(1)
print(d)

# Using a custom function as the default factory
def default_value():
    return "N/A"

d = defaultdict(default_value)
print(d["c"])

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before clear method: \n", numbers)
numbers.clear()
print ("numbers dictionary after clear method: \n", numbers)

# Creating a dictionary
student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}
# Removing items based on conditions
keys_to_remove = ["age", "major"]
for key in keys_to_remove:
    student_info.pop(key, None)

print(student_info)

student = {"name": "Alice", "age": 21, "major": "Computer Science"}
# Looping through key-value pairs
for key, value in student.items():
   print(key, value)
# Looping through keys
for key in student.keys():
   print(key)
# Looping through values
for value in student.values():
   print(value)

original_dict = {"name": "Alice", "age": 25, "skills": ["Python", "Data Science"]}
shallow_copy = original_dict.copy()
# Modifying the shallow copy
shallow_copy["age"] = 26
shallow_copy["skills"].append("Machine Learning")
print("Original dictionary:", original_dict)
print("Shallow copy:", shallow_copy)

import copy
original_dict = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Data Science"],
    "education": {
      "degree": "Bachelor's",
      "field": "Computer Science"
   }
}
# Creating a deep copy
deep_copy = copy.deepcopy(original_dict)
# Modifying the deep copy
deep_copy["age"] = 26
deep_copy["skills"].append("Machine Learning")
deep_copy["education"]["degree"] = "Master's"
# Retrieving both dictionaries
print("Original dictionary:", original_dict)
print("Deep copy:", deep_copy)

# Define a nested dictionary
students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"},
    "Charlie": {"age": 22, "major": "Mathematics"}
}
# Access Alice's major using .get()
alice_major = students.get("Alice", {}).get("major", "Not Found")
print("Alice's major:", alice_major)
# Safely access a non-existing key using .get()
dave_major = students.get("Dave", {}).get("major", "Not Found")
print("Dave's major:", dave_major)

# Define a nested dictionary
students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"},
    "Charlie": {"age": 22, "major": "Mathematics"}
}
# Delete the dictionary for Bob
del students["Bob"]
# Print the updated nested dictionary
print(students)

# Defining a nested dictionary
students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"},
    "Charlie": {"age": 22, "major": "Mathematics"}
}
# Iterating through the Nested Dictionary:
for student, details in students.items():
   print(f"Student: {student}")
   for key, value in details.items():
      print(f"  {key}: {value}")

# Dictionary Methods
# Sr.No.	Method and Description
# 1
# dict.clear()
# Removes all elements of dictionary dict.
#
# 2
# dict.copy()
# Returns a shallow copy of dictionary dict.
#
# 3
# dict.fromkeys()
# Create a new dictionary with keys from seq and values set to value.
#
# 4
# dict.get(key, default=None)
# For key key, returns value or default if key not in dictionary.
#
# 5
# dict.has_key(key)
# Returns true if a given key is available in the dictionary, otherwise it returns a false.
#
# 6
# dict.items()
# Returns a list of dict's (key, value) tuple pairs.
#
# 7
# dict.keys()
# Returns list of dictionary dict's keys.
#
# 8
# dict.pop()
# Removes the element with specified key from the collection
#
# 9
# dict.popitem()
# Removes the last inserted key-value pair
#
# 10
# dict.setdefault(key, default=None)
# Similar to get(), but will set dict[key]=default if key is not already in dict.
#
# 11
# dict.update(dict2)
# Adds dictionary dict2's key-values pairs to dict.
#
# 12
# dict.values()
# Returns list of dictionary dict's values.