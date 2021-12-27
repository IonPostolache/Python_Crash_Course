class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(f"This restaurant is called {self.restaurant_name.title()}.")
        print(f"This restaurant's cuisine is {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print("The restaurant is now open.")

mandachi=Restaurant('spartacus', 'greek')
print(f"{mandachi.restaurant_name.title()}")
print(f"{mandachi.cuisine_type.title()}")

mandachi.describe_restaurant()
mandachi.open_restaurant()


class IceCreamStand(Restaurant):
    def __init__(self, flavors):
        self.flavors=flavors

    def display_flavors(self):
        print(f"The flavors we have are: {self.flavors}.")

flavors2=['cherry', 'brocoly', 'peaches']
city_stand=IceCreamStand(flavors2)
city_stand.display_flavors()
