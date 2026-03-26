class Employee:
    'Common base class for all employees'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):
        print ("Name : ", self.name, ", Salary: ", self.salary)

# This would create first object of Employee class
emp1 = Employee("Zara", 2000)
print(emp1.name, emp1.salary)
# This would create second object of Employee class
emp2 = Employee("Manni", 5000)
print(emp2.name, emp2.salary)

emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)


class JustCounter:
    __secretCount = 0
    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()

# Modifying Class Attributes
class Employee:
   # class attribute
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      # modifying class attribute
      Employee.empCount += 1
      print ("Name:", self.__name, ", Age: ", self.__age)
      # accessing class attribute
      print ("Employee Count:", Employee.empCount)

e1 = Employee("Bhavana", 24)
print()
e2 = Employee("Rajesh", 26)

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )

class Student:
   def __init__(self, name, grade):
      self.__name = name
      self.__grade = grade
      print ("Name:", self.__name, ", Grade:", self.__grade)
# Creating instances
student1 = Student("Ram", "B")
student2 = Student("Shyam", "C")
print(student1, student2)


class Employee:
    empCount = 0
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Employee.empCount += 1
    def showcount(self):
        print(self.empCount)
    @classmethod
    def newemployee(cls, name, age):
        return cls(name, age)
    counter = classmethod(showcount)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)
e4 = Employee.newemployee("Anil", 21)

e1.showcount()
Employee.counter()

class Cloth:
   # Class attribute
   price = 4000
   @classmethod
   def showPrice(cls):
      return cls.price
# Accessing class attribute
print(Cloth.showPrice())

class Cloth:
   # class method
   @classmethod
   def brandName(cls):
      print("Name of the brand is Raymond")

# deleting dynamically
del Cloth.brandName
print("Method deleted")

class Employee:
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Employee.empCount += 1
    # creating staticmethod
   def showcount():
       print(Employee.empCount)
       return
   counter = staticmethod(showcount)
e1.counter()
Employee.counter()
