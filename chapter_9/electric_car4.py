class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
        self.tank_capacity=60

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading+=miles

    def fill_gas_tank(self, tank_capacity):
        print(f"This car has a {self.tank_capacity} litres tank capacity.")


my_new_car=Car('vw', 'passat', 2018)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(200)
my_new_car.read_odometer()

my_used_car=Car('opel', 'astra', 1992)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery'a attributes."""
        self.battery_size=battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize atributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery2=Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tank."""
        print("This car doesn't need a gas tank!")

my_tesla=ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
#my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery2.describe_battery()

#my_used_car.fill_gas_tank(63)
