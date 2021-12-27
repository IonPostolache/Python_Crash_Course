def greet_users(names):
    for name in names:
        msg=f"Hello {name.title()}!"
        print(msg)


usernames=['alfa', 'beta', 'omega']
greet_users(usernames)
