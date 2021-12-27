class User:
    """This is Users class"""
    def __init__(self, first_name, last_name, age, gender):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender

    def describe_user(self):
        print(f"\nThis user name is: "
            f"{self.first_name.title()} "
            f"{self.last_name.title()},")

        if self.gender=='m':
            print(f"He ")
        elif self.gender=='f':
            print("She")

        print(f"is {self.age} years old and "
            f"the gender is {self.gender.title()}.")

    def greet_user(self):
        print(f"Welcome on board, {self.first_name.title()}!")

first_user=User('elon', 'musk', 39, 'm')
first_user.describe_user()
first_user.greet_user()

second_user=User('aglaia', 'azanicai', 80, 'f')
second_user.describe_user()
second_user.greet_user()
