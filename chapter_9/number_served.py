class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print(f"This restaurant is called {self.restaurant_name.title()}.")
        print(f"This restaurant's cuisine is {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print("The restaurant is now open.")

    def number(self):
        print(f"This restaurant served {self.number_served} people.")

    def set_number_served(self, setted):
        self.number_served=setted
        print(f"{self.number_served} people have been served now.")

    def increment_number_served(self, incr):
        self.number_served+=incr
        print(f"{self.number_served} people have beeen served today.")

mandachi=Restaurant('spartacus', 'greek')
print(f"{mandachi.restaurant_name.title()}")
print(f"{mandachi.cuisine_type.title()}")

mandachi.describe_restaurant()
mandachi.open_restaurant()

restnt=Restaurant('jolly', 'jamaican')
restnt.number()
restnt.number_served=12
restnt.number()

restnt.set_number_served(24)
restnt.increment_number_served(10)
