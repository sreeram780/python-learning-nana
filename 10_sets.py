calculate_to_units = 24 * 60 # dynamically typed
name_of_unit = "minutes"

def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculate_to_units} {name_of_unit} "

def validate_and_execute(number_days):
    try:
        user_input_number = int(number_days)
        if user_input_number > 0:
            result = days_to_units(user_input_number)
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
    user_input = input(" Enter number of days as list to convert into minutes \n")
    print(user_input.split())
    print(type(user_input.split()))
    print(set(user_input.split()))
    print(type(set(user_input.split())))

    for number in set(user_input.split()):
        validate_and_execute(number)