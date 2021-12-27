my_foods=['pizza', 'falafel', 'carrot cake']
friends_food=my_foods[:]
my_foods.append('pie')
friends_food.append('eggs')
print(f"My favourtite foods are {my_foods}.")
print(f"My friend's favourite foods are {friends_food}.")

friends_food.append('chips')
print(f"My friend's favourite foods are {friends_food}.")

second_friend_food=['beans', 'sauce', 'sausage']

both_friends_food=friends_food+second_friend_food
print(f"My both friends favourite foods are {both_friends_food}.")

print(f"The first three items in the list are: {friends_food[0:3]}")
print(f"The middle three items of the list are {friends_food[1:4]}")
print(f"The last three items in the list are {friends_food[-3:]}")
