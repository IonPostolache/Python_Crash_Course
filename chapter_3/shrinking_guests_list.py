guests=['Albert', 'Elon', 'Nikola']

print(f"Hi {guests[0]}, would you like to have dinner with me?")
print(f"Hi {guests[1]}, would you like to have dinner with me?")
print(f"Hi {guests[2]}, would you like to have dinner with me?")

removed=guests[1]
print(f"I've just found out that {removed} can't make it.")
guests[1]='Stephan'
print(guests)


print(f"\nHi {guests[0]}, would you like to have dinner with me?")
print(f"Hi {guests[1]}, would you like to have dinner with me?")
print(f"Hi {guests[2]}, would you like to have dinner with me?")

print(f"Hi {guests[0]}, {guests[1]} and {guests[2]}, I just found a bigger table.")
guests.insert(0, 'Frank')
guests.insert(2, 'Napoleon')
guests.append('Agatha')

print(f"\nHi {guests[0]}, would you like to have dinner with me?")
print(f"Hi {guests[1]}, would you like to have dinner with me?")
print(f"Hi {guests[2]}, would you like to have dinner with me?")
print(f"Hi {guests[3]}, would you like to have dinner with me?")
print(f"Hi {guests[4]}, would you like to have dinner with me?")
print(f"Hi {guests[5]}, would you like to have dinner with me?")

print("\nHi, I can only invite two people for the dinner.")

first_removed=guests.pop()
print(f"Hi {first_removed}, I'm really sorry but I can't invite you this time.")
#print(guests)
second_removed=guests.pop()
print(f"Hi {second_removed}, I'm really sorry but I can't invite you this time.")
#print(guests)
third_removed=guests.pop()
print(f"Hi {third_removed}, I'm really sorry but I can't invite you this time.")
#print(guests)
fourth_removed=guests.pop()
print(f"Hi {fourth_removed}, I'm really sorry but I can't invite you this time.")
print(guests)

print(f"Hi {guests[0]}, I just wanted to remind you that you are still invited.")
print(f"Hi {guests[1]}, I just wanted to remind you that you are still invited.")

del guests[0]
print(guests)
del guests[0]
print(guests)
