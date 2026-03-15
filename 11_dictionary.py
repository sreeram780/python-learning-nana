calculate_to_units = 24 * 60 # dynamically typed
name_of_unit = "minutes"

def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * calculate_to_units} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * calculate_to_units} minutes"
    else:
        return "Unsupported Unit"

def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            result = days_to_units(user_input_number, days_and_unit_dictionary["units"])
            print(result)
        elif user_input_number == 0:
            print("Enter the positive number of days")
        else:
            print("No negetive nummber")
    except ValueError:
        print("Your input was not a number.")

# while True: // runs always because of True
user_input = ""
while user_input != "exit": # run until user gives exit as input
    user_input = input("Enter number of days and conversion unit \n")
    days_and_units = user_input.split(":")
    print(days_to_units)
    days_and_unit_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    print(days_and_unit_dictionary)
    validate_and_execute()