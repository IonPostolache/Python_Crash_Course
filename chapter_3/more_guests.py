guests=['Albert', 'Elon', 'Nikola']

message1=guests[0]
message2=guests[1]
message3=guests[2]

print(f"Hi {message1}, would you like to have dinner with me?")
print(f"Hi {message2}, would you like to have dinner with me?")
print(f"Hi {message3}, would you like to have dinner with me?")

removed=guests[1]
print(f"I've just found out that {removed} can't make it.")
guests[1]='Stephan'
print(guests)

message1=guests[0]
message2=guests[1]
message3=guests[2]

print(f"\nHi {message1}, would you like to have dinner with me?")
print(f"Hi {message2}, would you like to have dinner with me?")
print(f"Hi {message3}, would you like to have dinner with me?")

print(f"Hi {message1}, {message2} and {message3}, I just found a bigger table.")
guests.insert(0, 'Frank')
guests.insert(2, 'Napoleon')
guests.append('Agatha')
#print(guests)

print(f"\nHi {guests[0]}, would you like to have dinner with me?")
print(f"Hi {guests[1]}, would you like to have dinner with me?")
print(f"Hi {guests[2]}, would you like to have dinner with me?")
print(f"Hi {guests[3]}, would you like to have dinner with me?")
print(f"Hi {guests[4]}, would you like to have dinner with me?")
print(f"Hi {guests[5]}, would you like to have dinner with me?")
#print(f"Hi {guests[6]}, would you like to have dinner with me?")
