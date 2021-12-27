"""
prompt="\nTell me something:"
prompt+="\n Enter 'quit' to end. "
message=""
while message!='quit':
    message=input(prompt)
    if message!='quit':
        print(message)


prompt="\nTell me something:"
prompt+="\n Enter 'quit' to end. "
message=input(prompt)
while message!='quit':
    print(message)
"""

prompt="\nTell me something:"
prompt+="\n Enter 'quit' to end. "
active=True

while active:
    message=input(prompt)
    if message=='quit':
        active=False
    else:
        print(message)
