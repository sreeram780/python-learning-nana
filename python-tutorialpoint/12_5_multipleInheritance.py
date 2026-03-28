class Father:
    def skill1(self):
        print("Father's skill: Gardening")
class Mother:
    def skill2(self):
        print("Mother's skill: Cooking")
class Child(Father, Mother):
    pass
c = Child()
c.skill1()
c.skill2()

# # Method Resolution Order (MRO)
# First, Python looks for the method in the child class itself.
# If not found, it searches the parent classes in the order they are listed.
# This continues until the method is found or all classes have been searched.
class Father:
    def skill(self):
        print("Father's skill: Gardening")
class Mother:
    def skill(self):
        print("Mother's skill: Cooking")
class Child(Father, Mother):
    pass
c = Child()
c.skill()

# super calling parent in child class
class A:
    def show(self):
        print("Class A")
class B(A):
    def show(self):
        print("Class B")
        super().show()
class C(A):
    def show(self):
        print("Class C")
        super().show()
class D(B, C):
    def show(self):
        print("Class D")
        super().show()
d = D()
d.show()

class A:
    def show(self):
        print("Class A")
class B(A):
    def show(self):
        print("Class B")
class C(A):
    def show(self):
        print("Class C")
class D(B, C):
    pass
d = D()
d.show()