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


class Privileges:
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges=privileges

    def show_privileges(self):
        print(f"The admin's privileges are: {self.privileges}.")

class Admin(User):
    """writing a class that inherits from the 'User' class."""
    def __init__(self):
        self.privileges=Privileges()

admin_instance=Admin()
admin_instance.privileges.show_privileges()
