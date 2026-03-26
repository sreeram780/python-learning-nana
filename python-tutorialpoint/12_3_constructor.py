# Default Constructor in Python
class Employee:
   'Common base class for all employees'
   def __init__(self):
      self.name = "Bhavana"
      self.age = 24

e1 = Employee()
print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))

# Parameterized Constructor
class Employee:
   'Common base class for all employees'
   def __init__(self, name, age):
      self.name = name
      self.age = age

e1 = Employee("Bhavana", 24)
e2 = Employee("Bharat", 25)

print ("Name: {} age: {}".format(e1.name, e1.age))
print ("Name: {} age: {}".format(e2.name, e2.age))

#  with default params
class Employee:
   'Common base class for all employees'
   def __init__(self, name="Bhavana", age=24):
      self.name = name
      self.age = age

e1 = Employee()
e2 = Employee("Bharat", 25)

print ("Name: {} age: {}".format(e1.name, e1.age))
print ("Name: {} age: {}".format(e2.name, e2.age))

# Instant methods
class Employee:
   def __init__(self, name="Bhavana", age=24):
      self.name = name
      self.age = age
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.age)

e1 = Employee()
e2 = Employee("Bharat", 25)

e1.displayEmployee()
e2.displayEmployee()
# Returns true if 'salary' attribute exists
print (hasattr(e1, 'salary'))
# Returns value of 'name' attribute
print (getattr(e1, 'name'))
# Set attribute 'salary' at 8
setattr(e1, 'salary', 7000)
# Delete attribute 'age'
delattr(e1, 'age')

# Python Multiple Constructors
class Student:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]
        elif len(args) == 3:
            self.name = args[0]
            self.age = args[1]
            self.gender = args[2]
st1 = Student("Shrey")
print("Name:", st1.name)
st2 = Student("Ram", 25)
print(f"Name: {st2.name} and Age: {st2.age}")
st3 = Student("Shyam", 26, "M")
print(f"Name: {st3.name}, Age: {st3.age} and Gender: {st3.gender}")

# Access Modifiers in Python
class Employee:
   def __init__(self, name, age, salary):
      self.name = name # public variable
      self.__age = age # private variable
      self._salary = salary # protected variable
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)
e1=Employee("Bhavana", 24, 10000)
print (e1.name)
print (e1._salary)

# Name Mangling
# obj._class__privatevar
print (e1._Employee__age)

# Getters and Setter Methods
class Employee:
   def __init__(self, name, age):
      self.__name = name
      self.__age = age

   def get_name(self):
      return self.__name
   def get_age(self):
      return self.__age
   def set_name(self, name):
      self.__name = name
      return
   def set_age(self, age):
      self.__age=age
      return
   name = property(get_name, set_name, "name")
   age = property(get_age, set_age, "age")

e1=Employee("Bhavana", 24)
print ("Name:", e1.name, "age:", e1.age)

e1.name = "Archana"
e1.age = 23
print ("Name:", e1.name, "age:", e1.age)