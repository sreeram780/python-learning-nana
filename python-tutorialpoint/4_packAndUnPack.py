
# Packing Example
def pack_example(*args):
    print("Packed arguments:", args)
pack_example(1, 2, 3, 'a', 'b')

# Unpacking Example
def unpack_example(a, b, c):
    print("Unpacked arguments:", a, b, c)
values = [1, 2, 3]
unpack_example(*values)

# Packing a tuple
my_tuple = (1, 2, 3)

# Unpacking a tuple
a, b, c = my_tuple

tup1 = (10,20,30, 40, 50, 60)
x, *y, z = tup1
print ("x: ",x, "y: ", y, "z: ", z)

tup1 = (10,20,30, 40, 50, 60)
*x, y, z = tup1
print ("x: ",x, "y: ", y, "z: ", z)

def pack_args(*args):
    print("Packed arguments:", args)

# Calling the function with multiple arguments
pack_args(1, 2, 3, 'a', 'b')

def pack_kwargs(**kwargs):
    print("Packed keyword arguments:", kwargs)

# Calling the function with multiple keyword arguments
pack_kwargs(name="Alice", age=30, city="New York")


def unpack_kwargs(name, age, city):
    print("Unpacked keyword arguments:", name, age, city)

# Dictionary of values to unpack
info = {"name": "Farhan", "age": 25, "city": "Los Angeles"}

# Calling the function with unpacked values
unpack_kwargs(**info)

# Function that accepts variable number of items (packing with *args)
def calculate_total(*items):
    print("Items in cart:", items)
    return sum(items)

# Function that accepts variable keyword arguments (packing with **kwargs)
def print_invoice(customer_name, **details):
    print(f"Invoice for {customer_name}")
    for key, value in details.items():
        print(f"{key}: {value}")

# _ Unpacking Example _

# Order items (list of prices)
order_items = [250, 100, 75]   # Prices of products
total_amount = calculate_total(*order_items)   # Unpacking list
print("Total Amount:", total_amount)

# Order details (dictionary)
order_details = {
    "Product": "Laptop",
    "Quantity": 1,
    "Price": total_amount,
    "Payment Method": "Credit Card"
}

# Passing dictionary as keyword args
print_invoice("Farhan", **order_details)