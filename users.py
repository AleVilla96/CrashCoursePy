"""A class that can be used to represent a user"""

class User:
    def __init__(self, first_name, last_name, age, doc_number):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.doc_number = doc_number
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_ogin_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Doc Number: {self.doc_number}")

    def greet_user(self):
        print(f"Greetings {self.first_name} {self.last_name}!!")

usr1 = User("Ale", "Villa", 28, 39796715)
usr1.greet_user()
usr1.describe_user()

usr1.increment_login_attempts()
usr1.increment_login_attempts()
usr1.increment_login_attempts()
usr1.increment_login_attempts()

print(f"Login Attempts: {usr1.login_attempts}")
usr1.reset_ogin_attempts()
print(f"Login Attempts: {usr1.login_attempts}")

print("\n")
