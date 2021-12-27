fav_numbers={'ben':[6, 2], 'sam':[12], 'kiran':[7], 'raj':[4], 'sully':[10]}

#print(f"{fav_numbers[0]}favorite number is {fav_numbers['ben']}.")
for name, number in fav_numbers.items():
    #print(f"{name.title()}'s favorite number is {number}.")
    print(f"{name.title()}: ")
    for n in number:
        print(f"    {n}")
