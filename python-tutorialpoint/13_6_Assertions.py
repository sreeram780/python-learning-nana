# assert
# assert condition, message

print('Enter marks out of 100:')
num = 75
assert num >= 0 and num <= 100
print('Marks obtained:', num)

num = 125
assert num >= 0 and num <= 100
print('Marks obtained:', num)  # This line won't be reached if assertion fails

# Custom Error Messages
assert num >= 0 and num <= 100, "Only numbers in the range 0-100 are accepted"

# Handling AssertionError
try:
   num = int(input('Enter a number: '))
   assert num >= 0, "Only non-negative numbers are accepted"
   print(num)
except AssertionError as msg:
   print(msg)