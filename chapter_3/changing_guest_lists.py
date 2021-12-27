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
