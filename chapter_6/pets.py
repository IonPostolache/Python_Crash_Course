azor={'kind_of_animal':'dog', 'owner':'mitica'}
neculai={'kind_of_animal':'cat', 'owner':'grigore'}
urechila={'kind_of_animal':'rabbit', 'owner':'culitza'}

pets=[azor, neculai, urechila]

for every_pet in pets:
    for a, b in every_pet.items():
        print(f"{a.title()} is {b.title()}")
        print("\n")
