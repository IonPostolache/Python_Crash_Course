prompt='please type your age! '
prompt+='\ntype quit to end the program: '

while message!='quit':
    message=input(prompt)
    if int(message)<3:
        print("You can watch the movie for free!")
    elif int(message)<=12:
        print("£10 please!")
    elif int(message)>12:
        print("£15 please!")
"""
game=True
while game:
    message=input(prompt)
    if message=='quit':
        game=False
    elif int(message)<3:
        print("You can watch the movie for free!")
    elif int(message)<=12:
        print("£10 please!")
    elif int(message)>12:
        print("£15 please!")

while True:
    message=input(prompt)
    if message=='quit':
        break
    elif int(message)<3:
        print("You can watch the movie for free!")
    elif int(message)<=12:
        print("£10 please!")
    elif int(message)>12:
        print("£15 please!")
"""
