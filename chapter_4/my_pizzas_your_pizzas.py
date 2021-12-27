pizzas=['original cheese', 'marguerita', 'quatro formagi']
for every_pizza in pizzas:
    #print(every_pizza.title())
    print(f"I like {every_pizza} pizza.")

print(f"""\n\tI like pizza very much, I like {pizzas[0]},
    \n\tI like {pizzas[1]}, {pizzas[2]},
    \n\tI really love pizza!""")

friend_pizza=pizzas[:]
pizzas.append('diabolo')
friend_pizza.append('italiano')

print(f"My favourite pizzas are {pizzas}.")
print(f"My friend's favourite pizzas are {friend_pizza}")
print(f"My favourite pizzas are: ")
for piz in pizzas:
    print(piz)

print(f"My friend's favourite pizzas are:")
for frpz in friend_pizza:
    print(frpz)
