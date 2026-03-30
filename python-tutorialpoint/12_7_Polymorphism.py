# Duck Typing
# Duck typing is a concept where the type or class of an object is less important than the methods it defines. Using this concept, you can call any method on an object without checking its type, as long as the method exists.
class Duck:
   def sound(self):
      return "Quack, quack!"
class AnotherBird:
   def sound(self):
      return "I'm similar to a duck!"
def makeSound(duck):
   print(duck.sound())
# creating instances
duck = Duck()
anotherBird = AnotherBird()
# calling methods
makeSound(duck)
makeSound(anotherBird)

# Operator Overloading
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)

# Method Overriding
# In method overriding, a method defined inside a subclass has the same name as a method in its superclass but implements a different functionality.
from abc import ABC, abstractmethod
class shape(ABC):
   @abstractmethod
   def draw(self):
      "Abstract method"
      return
class circle(shape):
   def draw(self):
      super().draw()
      print ("Draw a circle")
      return
class rectangle(shape):
   def draw(self):
      super().draw()
      print ("Draw a rectangle")
      return
shapes = [circle(), rectangle()]
for shp in shapes:
   shp.draw()

# Method Overloading
def add(*nums):
   return sum(nums)
# Call the function with different number of parameters
result1 = add(10, 25)
result2 = add(10, 25, 35)

print(result1)
print(result2)

# Implement Method Overloading Using MultipleDispatch
from multipledispatch import dispatch
class example:
   @dispatch(int, int)
   def add(self, a, b):
      x = a+b
      return x
   @dispatch(int, int, int)
   def add(self, a, b, c):
      x = a+b+c
      return x
obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20))