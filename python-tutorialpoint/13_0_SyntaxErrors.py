# # Error: Missing colon (:) after the if statement
# if True
#    print("This will cause a syntax error")
#
# # Error: The print statement is not correctly indented
# def example_function():
# print("This will cause a syntax error")
#
# # Error: 'print' is misspelled as 'prnt'
# prnt("Hello, World!")
#
# # Error: The closing parenthesis is missing.
# print("This will cause a syntax error"

# assertion syntax
#   assert Expression[, Arguments]
def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32
print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
# print (KelvinToFahrenheit(-5))

# Handling an Exception in Python
# The try: block contains statements which are susceptible for exception
# If exception occurs, the program jumps to the except: block.
# If no exception in the try: block, the except: block is skipped

# try:
#    You do your operations here
#    ......................
# except ExceptionI:
#    If there is ExceptionI, then execute this block.
# except ExceptionII:
#    If there is ExceptionII, then execute this block.
#    ......................
# else:
#    If there is no exception then execute this block.

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()

#  try except else
try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")

#  try except finally
try:
   fh = open("testfile", "w")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print ("Going to close the file")
      fh.close()
except IOError:
   print ("Error: can\'t find file or read data")

# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError as Argument:
      print ("The argument does not contain numbers\n", Argument)
# Call above function here.
temp_convert("xyz")

# User-Defined Exceptions
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg

try:
   raise Networkerror("Bad hostname")
except Networkerror as e:
   print (e)