
# type() Function
print (type(10))
print (type(2.56))
print (type(2+3j))
print (type("Hello World"))
print (type([1,2,3]))
print (type({1:'one', 2:'two'}))
class test:
    pass
obj = test()
print(type(obj))

# isinstance() Function
print (isinstance(10, int))
print (isinstance(2.56, float))
print (isinstance(2+3j, complex))
print (isinstance("Hello World", str))
print (isinstance([1,2,3], tuple))
print (isinstance({1:'one', 2:'two'}, set))
class test:
    pass
obj = test()
print(isinstance(obj, test))

# issubclass() Function
class test:
    pass
obj = test()
print(isinstance(obj, test))

# callable() Function
def test():
    pass
print(callable("Hello"))
print(callable(abs))
print(callable(list.clear([1, 2])))
print(callable(test))

# getattr() Function
class test:
    def __init__(self):
        self.name = "Manav"
obj = test()
print(getattr(obj, "name"))

# setattr() Function
class test:
    def __init__(self):
        self.name = "Manav"
obj = test()
setattr(obj, "age", 20)
setattr(obj, "name", "Madhav")
print(obj.name, obj.age)

# hasattr() Function
class test:
    def __init__(self):
        self.name = "Manav"
obj = test()
print(hasattr(obj, "age"))
print(hasattr(obj, "name"))

# dir() Function
print ("dir(int):", dir(int))


#  with data class
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    percent: float = 0.0  # Default value for percent

s1 = Student("Alice", 20)
s2 = Student("Bob", 22, 85.5)
print(s1)
print(s2)
# without data class
class Student:
    def __init__(self, name: str, age: int, percent: float):
        self.name = name
        self.age = age
        self.percent = percent
    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, percent={self.percent})"
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return (self.name == other.name and self.age == other.age and self.percent == other.percent)
s1 = Student("Alice", 20, 90.0)
s2 = Student("Bob", 22, 85.5)
print(s1)
print(s1 == s2)