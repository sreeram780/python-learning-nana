# import single or double function
from helper import validate_and_execute, user_input_message
# import many
# from  helper import  *
# import entire module
# import  itemlogger

# import entire module rename
import  itemlogger as loggr

import os

print(os.name)

user_input = ""
while user_input != "exit": # run until user gives exit as input
    user_input = input(user_input_message)
    days_and_units = user_input.split(":")
    print(days_and_units)
    days_and_unit_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    print(days_and_unit_dictionary)
    validate_and_execute(days_and_unit_dictionary)
    loggr.print_items(days_and_unit_dictionary)