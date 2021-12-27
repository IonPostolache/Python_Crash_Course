class User:
    """This is Users class"""
    def __init__(self, first_name, last_name, age, gender):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.login_attempts=0

    def describe_user(self):
        print(f"\nThis user name is: "
            f"{self.first_name.title()} "
            f"{self.last_name.title()},")
        print(f"is {self.age} years old and "
            f"the gender is {self.gender.title()}.")

    def greet_user(self):
        print(f"Welcome on board, {self.first_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts+=1
        print(f"The incremented value is: {self.login_attempts}.")

    def reset_login_attempts(self):
        self.login_attempts=0
        print(f"The value after reset to zero is: {self.login_attempts}.")


first_user=User('elon', 'musk', 39, 'm')
first_user.describe_user()
first_user.greet_user()

second_user=User('aglaia', 'azanicai', 80, 'f')
second_user.describe_user()
second_user.greet_user()

third_user=User('jica', 'budescu', 41, 'm')
third_user.increment_login_attempts()
third_user.increment_login_attempts()
third_user.increment_login_attempts()
print(third_user.login_attempts)
third_user.reset_login_attempts()
print(third_user.login_attempts)


class Admin(User):
    """writing a class that inherits from the 'User' class."""
    def __init__(self, privileges):
        self.privileges=privileges

    def show_privileges(self):
        print(f"The admin's privileges are: {self.privileges}.")

privileges2=['can add post', 'can delete post', 'can ban user']
gogu=Admin(privileges2)
gogu.show_privileges()
