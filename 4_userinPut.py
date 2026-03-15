calculate_to_units = 24 * 60 # dynamically typed
name_of_unit = "minutes"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculate_to_units} {name_of_unit} "

user_input = input(" Enter number of days to convert into minutes \n")
value = days_to_units(int(user_input))
print(value)