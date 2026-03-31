class Student:
   def __init__(self, name="Rajaram", marks=50):
      self.name = name
      self.marks = marks

s1 = Student()
s2 = Student("Bharat", 25)

print ("Name: {} marks: {}".format(s1.name, s2.marks))
print ("Name: {} marks: {}".format(s2.name, s2.marks))

#  Encapsulation
class Student:
    def __init__(self, name="Rajaram", marks=50):
        self.__name = name
        self.__marks = marks
    def studentdata(self):
        print("Name: {} marks: {}".format(self.__name, self.__marks))
s1 = Student()
s2 = Student("Bharat", 25)

s1.studentdata()
s2.studentdata()
print("Name: {} marks: {}".format(s1._Student__name, s1._Student__marks))
print("Name: {} marks: {}".format(s2._Student__name, s2._Student__marks))