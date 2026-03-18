# lamda and list
original_list = [1, 2, 3, 4, 5]
doubled_list = [(lambda x: x * 2)(x) for x in original_list]
print(doubled_list)

# Nested Loops in Python List Comprehension
list1=[1,2,3]
list2=[4,5,6]
CombLst=[(x,y) for x in list1 for y in list2]
print (CombLst)

# Conditionals in Python List Comprehension
list1=[x for x in range(1,21) if x%2==0]
print (list1)

# List Comprehensions vs For Loop
chars=[]
for ch in 'TutorialsPoint':
   if ch not in 'aeiou':
      chars.append(ch)
print (chars)

chars = [ char for char in 'TutorialsPoint' if char not in 'aeiou']
print (chars)

# Conciseness − List comprehensions are more concise and readable compared to traditional for loops, allowing you to create lists with less code.
#
# Efficiency − List comprehensions are generally faster and more efficient than for loops because they are optimized internally by Python's interpreter.
#
# Clarity − List comprehensions result in clearer and more expressive code, making it easier to understand the purpose and logic of the operation being performed.
#
# Reduced Chance of Errors − Since list comprehensions are more compact, there is less chance of errors compared to traditional for loops, reducing the likelihood of bugs in your code.