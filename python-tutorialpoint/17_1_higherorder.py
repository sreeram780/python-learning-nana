# Higher order function
# A function can be stored in a variable.
# A function can be passed as a parameter to another function.
# A high order functions can be stored in the form of lists, hash tables, etc.
# Function can be returned from a function.

# Creating Higher-Order Functions with Callable Objects
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, x):
        return self.factor * x
# Create an instance of the Multiplier class
multiply_second_number = Multiplier(2)

# Call the  Multiplier object to computes factor * x
Result = multiply_second_number(100)
# Printing result
print("Multiplication of Two numbers is: ", Result)

# Higher-order functions with the 'functools' Module
import functools
def my_decorator(f):
   @functools.wraps(f)
   def wrapper(*args, **kwargs):
      print("Calling", f.__name__)
      return f(*args, **kwargs)
   return wrapper
@my_decorator
def invite(name):
   print(f"Welcome to, {name}!")
invite("Tutorialspoint")

# Working with Higher-order functions using the partial()
import functools
def myfunction(a,b):
   return a*b
partfunction = functools.partial(myfunction,b = 10)
print(partfunction(10))

# Working with Higher-order functions using the reduce()
import functools
def mult(x,y):
   return x*y
# Define a number to calculate factorial
n = 4
num = functools.reduce(mult, range(1, n+1))
print (f'Factorial of {n}: ',num)