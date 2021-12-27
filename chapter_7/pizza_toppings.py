prompt='enter some pizza toppings please: '
message=[]
while message!='quit':
    message=input(prompt)
    print(f"{message.title()} topping has been added to your pizza.")
