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