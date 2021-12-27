#loop that never ends
prompt='please type a number: '

message=input(prompt)

while int(message)<5:
    print("Your number is smaller than 5.")
