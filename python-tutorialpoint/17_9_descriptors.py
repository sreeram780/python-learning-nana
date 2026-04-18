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