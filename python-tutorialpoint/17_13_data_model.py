# __repr__(self) − It Returns an official string representation of the object. It is mainly used for debugging.
# __str__(self) − It Returns an human-readable representation of the object, which is displayed when we use print() or str().

class demo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

v = demo(3, 5)
print(v)
print(repr(v))


# Arithmetic Operations
class demo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return demo(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return demo(self.x * scalar, self.y * scalar)

x1 = demo(2, 3)
x2 = demo(4, 5)
print(x1 + x2)
print(x1 * 2)

# We will implement the __len__() for len(object).
# We will implement the __bool__() for the boolean evaluation.

import math
class demo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    def __add__(self, other):
        return demo(self.x + other.x, self.y + other.y)
    def __mul__(self, scalar):
        return demo(self.x * scalar, self.y * scalar)
    def __len__(self):
        return 2
    def __bool__(self):
        return bool(math.hypot(self.x, self.y))
v = demo(0, 0)
print(bool(v))
v = demo(3, 4)
print(bool(v))

# Equality Comparison
class demo:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
v1 = demo(2, 3)
v2 = demo(2, 3)
print(v1 == v2)