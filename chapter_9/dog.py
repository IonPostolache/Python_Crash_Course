class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} is now rolling over.")


my_dog=Dog('Willie', 5)
his_dog=Dog('Azor', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {his_dog.age} years old.")

my_dog.sit()
his_dog.roll_over()
