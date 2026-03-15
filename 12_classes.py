
class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def display(self):
        print(f"{self.first_name} {self.last_name} {self.age}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name} {self.age}")

    def update_age(self, new_age):
        self.age = new_age

    def increment_age(self):
        self.age += 1

user_one = User("John", "Doe", 1)
user_one.display()
