import datetime

user_input = input("Enter your goal separated by colon. \n")
inputs_list = user_input.split(":")
goal = inputs_list[0]
deadline = inputs_list[1]
deadline_date = datetime.datetime.strptime(deadline,"%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_date - today_date
# calculate how many days from now to deadline
print(f"Dear user!, Time remaining for your goal:{goal} is {time_till.days} days")
print(f"Dear user!, Time remaining for your goal:{goal} is {time_till.total_seconds() / 60} minutes")
print(f"Dear user!, Time remaining for your goal:{goal} is {time_till.total_seconds() / 60 / 60} hours")


