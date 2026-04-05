import warnings
# Normal message
print("TutorialsPoint")
# Warning message
# warnings.warn("You got a warning!")
# UserWarning Class
# warnings.warn("You got a warning!", UserWarning)
# DeprecationWarning Class
# warnings.warn("This feature is deprecated!", DeprecationWarning)

# SyntaxWarning Class
# Warning message
# warnings.warn("This is a syntax warning!", SyntaxWarning)
# Function with potential syntax issue
def func(x):
    return x is 10  # using "is" instead of "=="

# RuntimeWarning
# warnings.warn("This is a runtime warning!", RuntimeWarning)

# ImportWarning
warnings.warn("This is an import warning!", ImportWarning)

# warnings.warn(message, category=None, stacklevel=1, source=None, *, skip_file_prefixes=())