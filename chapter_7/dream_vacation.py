prompt='If you could visit one place in the world, where would you go?'
users={}
active=True
while active:
    user=input("What's your name? ")
    place=input(prompt)
    users[user]=place
    print("Would you like to ask more users?")
    continuation=input( )

    if continuation=='no':
        active=False


print("Below are the poll results:")
for u, p in users.items():
    print(f"{u.title()} would like to visit {p.title()}.")
