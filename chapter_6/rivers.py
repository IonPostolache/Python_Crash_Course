rivers={'nile': 'egypt', 'amazon': 'south_america', 'yamgtze':'china'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river1 in rivers.keys():
    print(f"{river1.title()}")

for country2 in rivers.values():
    print(f"{country2.title()}")

    
