
calculate_to_units = 24 * 60 # dynamically typed
name_of_unit = "minutes"
user_input_message = "Enter number of days and conversion unit \n"

def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * calculate_to_units} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * calculate_to_units} minutes"
    else:
        return "Unsupported Unit"

def validate_and_execute(days_and_unit_dictionary):
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

