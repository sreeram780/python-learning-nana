# Types of Python Abstraction
# There are two types of abstraction.
# One is data abstraction, wherein the original data entity is hidden via a data structure that can internally work through the hidden data entities.
# Another type is called process abstraction. It refers to hiding the underlying implementation details of a process.

from abc import ABC, abstractmethod
class democlass(ABC):
    @abstractmethod
    def method1(self):
        print("abstract method")
        return
    def method2(self):
        print("concrete method")
class concreteclass(democlass):
    def method1(self):
        super().method1()
        return
obj = concreteclass()
obj.method1()
obj.method2()