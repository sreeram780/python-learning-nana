
# Using % operator
name = "Tutorialspoint"
print("Welcome to %s!" % name)

# Using format() method
str = "Welcome to {}"
print(str.format("Tutorialspoint"))

# Using f-string
item1_price = 2500
item2_price = 300
total = f'Total: {item1_price + item2_price}'
print(total)

# Using String Template class

from string import Template
# Defining template string
str = "Hello and Welcome to $name !"
# Creating Template object
templateObj = Template(str)

# now provide values
new_str = templateObj.substitute(name="Tutorialspoint")
print(new_str)

# Escape Character
normal = "Hello\nWorld"
print (normal)

raw = r"Hello\nWorld"
print (raw)

# ignore \
s = 'This string will not include \
backslashes or newline characters.'
print (s)

# escape backslash
s=s = 'The \\character is called backslash'
print (s)

# escape single quote
s='Hello \'Python\''
print (s)

# escape double quote
s="Hello \"Python\""
print (s)

# escape \b to generate ASCII backspace
s='Hel\blo'
print (s)

# ASCII Bell character
s='Hello\a'
print (s)

# newline
s='Hello\nPython'
print (s)

# Horizontal tab
s='Hello\tPython'
print (s)

# form feed
s= "hello\fworld"
print (s)

# Octal notation
s="\101"
print(s)

# Hexadecimal notation
s="\x41"
print (s)