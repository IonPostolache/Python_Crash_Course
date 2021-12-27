print("deli has run out of pastrami")

sandwich_orders=['pastrami','dbl egg', 'pastrami', 'blt', 'pastrami', 'sausage']
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches=[]
while sandwich_orders:
    current_sandwich=sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)


print(f"I made for you the following sandwiches: ")
for every_finished_sandwich in finished_sandwiches:
    print(f"\t{every_finished_sandwich.title()}")
