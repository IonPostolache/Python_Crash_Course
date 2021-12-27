class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(f"\nThis restaurant is called {self.restaurant_name.title()}.")
        print(f"This restaurant's cuisine is {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print("\nThe restaurant is now open.")

mandachi=Restaurant('spartacus', 'greek')
mandachi.describe_restaurant()

barladeanu=Restaurant('moldova', 'moldovean')
barladeanu.describe_restaurant()

stoica=Restaurant('occident', 'seafruit')
stoica.describe_restaurant()
