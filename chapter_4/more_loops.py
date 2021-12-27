my_foods=['pizza', 'falafel', 'carrot cake']
friends_food=my_foods[:]
my_foods.append('pie')
friends_food.append('eggs')
print(f"My favourite foods are {my_foods}.")
print(f"My friend's favourite foods are {friends_food}.")

friends_food.append('chips')
print(f"My friend's favourite foods are {friends_food}.")

second_friend_food=['beans', 'sauce', 'sausage']

both_friends_food=friends_food+second_friend_food
print(f"My both friends favourite foods are {both_friends_food}.")

for food in my_foods:
    print(food)

for fr_food in friends_food:
    print(fr_food)
