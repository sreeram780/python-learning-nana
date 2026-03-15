calculate_to_units = 24 * 60 # dynamically typed
name_of_unit = "minutes"


def days_to_units():
    print(f"20 days are {20 * calculate_to_units} {name_of_unit} ")
    print("All good")

days_to_units()

# function with params
def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculate_to_units} {name_of_unit} ")

days_to_units(40)
days_to_units(50)
days_to_units(70)
days_to_units(140)

# function with more params
def days_to_units(num_of_days, dayd):
    print(f" {dayd} {num_of_days} days are {num_of_days * calculate_to_units} {name_of_unit} ")

days_to_units(40, "hi")
#  scope of variable
# A variable is only available from inside the region it is created
#  - Global scope = variable available from within any scope
#  - Local scope = variables created inside functions

def scope_check(num_of_days):
    my_var = "var in side function"
    print(my_var)
    print(num_of_days)
    print(name_of_unit)

scope_check(30)