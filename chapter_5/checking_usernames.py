current_users=['john', 'mark', 'steve', 'andy', 'kiran']
new_users=['ben', 'jack', 'will', 'sam', 'steve']
"""
for every_new_user in new_users:
    if every_new_user.lower() in current_users:
        print("Please enter a new username!")
    else:
        print("This username is available.")
"""
copy_of_current_users=current_users[:]
for every_new_user in new_users:
    if every_new_user in copy_of_current_users:
        print("Please enter a new username!")
    else:
        print("This username is available.")
