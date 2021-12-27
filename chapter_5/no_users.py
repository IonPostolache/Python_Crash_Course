#usernames=['john', 'mark', 'admin', 'steve']
usernames=[]

if usernames == []:
    print("We need to find some users")
else:
    for every_user in usernames:
        if every_user == 'admin':
            print(f"Hello {every_user}, would you like to see a status report?")
        else:
            print(f"Hello {every_user}, thank you for logging again.")
