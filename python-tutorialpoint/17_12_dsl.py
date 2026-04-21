# External DSL
# SELECT name FROM users WHERE age > 10;
# <h1>Welcome To Tutorialspoint</h1>

# Internal DSL
# @app.route('/home')
# def home():
#     return "Hello...!"

# Example 1
def add(x, y):
    return x + y
def multiply(x, y):
    return x * y
print(add(multiply(1, 3), multiply(2, 4)))