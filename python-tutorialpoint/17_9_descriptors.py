class LoggedDescriptor:
   def __init__(self, name):
      self.name = name

   def __get__(self, instance, owner):
      return instance.__dict__.get(self.name)

   def __set__(self, instance, value):
      instance.__dict__[self.name] = value

   def __delete__(self, instance):
      if self.name in instance.__dict__:
         print(f"Deleting {self.name} from {instance}")
         del instance.__dict__[self.name]
      else:
         raise AttributeError(f"{self.name} not found")

class Person:
   name = LoggedDescriptor("name")
   age = LoggedDescriptor("age")

   def __init__(self, name, age):
      self.name = name
      self.age = age

# Example usage
p = Person("Tutorialspoint", 30)
print(p.name)
print(p.age)

del p.name
print(p.name)

del p.age
print(p.age)

# Data descriptor
class Integer:
   def __get__(self, instance, owner):
      print("Getting value")
      return instance._value

   def __set__(self, instance, value):
      print("Setting value")
      if not isinstance(value, int):
         raise TypeError("Value must be an integer")
      instance._value = value

   def __delete__(self, instance):
      print("Deleting value")
      del instance._value
class MyClass:
   attr = Integer()
# Usage
obj = MyClass()
obj.attr = 42
print(obj.attr)
obj.attr = 100
print(obj.attr)
del obj.attr

# Non Data Descriptors
class Default:
   def __init__(self, default):
      self.default = default

   def __get__(self, instance, owner):
      return getattr(instance, '_value', self.default)

class MyClass:
   attr = Default("default_value")

# Usage
obj = MyClass()
print(obj.attr)
obj._value = "Tutorialspoint"
print(obj.attr)