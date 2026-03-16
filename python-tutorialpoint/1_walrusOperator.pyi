
# Traditional way
print("Using traditional way:")
stack = [1, 2, 3, 4, 5]
n = len(stack)
while len(stack) > 0:
    print(stack.pop(), end=" ")
print("\n\n")

# Simplify using walrus operator
print("Using walrus operator:")
stack = [1, 2, 3, 4, 5]
while (n := len(stack)) > 0:
    print(stack.pop(), end=" ")