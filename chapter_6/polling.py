favorite_language={
    'jason': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

sarah_fav=favorite_language['sarah'].title()
print(f"Sarah's favorite language is {sarah_fav}.")

people=['bob', 'bill', 'sarah', 'phil']

for every_people in people:
    if every_people in favorite_language.keys():
        print(f"Thanks for responding, {every_people.title()}!")
    elif every_people not in favorite_language.keys():
        print(f"You are invites to take the poll, {every_people.title()}!")
