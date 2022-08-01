class User:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and is from {self.country}")

    def greet_user(self):
        print(f"Hello {self.first_name}, how are you?")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_01 = User("Bethel", "Melesse", 25, "Ethiopia")
user_02 = User("Akhil", "Kedia", 27, "India")

user_01.describe_user()
user_01.greet_user()

user_02.describe_user()
user_02.greet_user()

user_01.increment_login_attempts()
user_01.increment_login_attempts()
user_01.increment_login_attempts()
print(user_01.login_attempts)

user_01.reset_login_attempts()
print(user_01.login_attempts)
