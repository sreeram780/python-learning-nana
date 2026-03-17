# Function definition is here
#  Positional or required Arguments
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;
# Now you can call printme function
# mandatory to pass value
printme("cc")

# Keyword Arguments
# Now you can call printme function
# specify argument name
printme( str = "My string")
# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )

# Default Arguments
# Function definition is here
def printinfodefaultArg( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfodefaultArg( age=50, name="miki" )
printinfodefaultArg( name="miki" )

# Positional-only arguments
"""Those arguments that can only be specified by their position in the function call is called as Positional-only arguments. 
They are defined by placing a "/" in the function's parameter list after all positional-only parameters.
This feature was introduced with the release of Python 3.8."""
def posFun(x, y, /, z):
    print(x + y + z)

print("Evaluating positional-only arguments: ")
posFun(33, 22, z=11)

# Keyword-only arguments

def posFun2(*, num1, num2, num3):
    print(num1 * num2 * num3)

print("Evaluating keyword-only arguments: ")
posFun2(num1=6, num2=8, num3=5)

# Arbitrary or Variable-length Arguments
"""You may need to process a function for more arguments than you specified while defining the function. 
These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments."""

def functionname([formal_args,] *var_args_tuple ):
   "function_docstring"
   function_suite
   return [expression]
# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )

# Lamda functions
# lambda [arg1 [,arg2,.....argn]]:expression
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))