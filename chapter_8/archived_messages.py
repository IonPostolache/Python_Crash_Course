def show_messages(message_list):
    print("These are the messages: ")
    for every_message in message_list:
        print(f"\t{every_message.title()}.")


def send_messages(message_list, sent_messages):
    print(f"Moving message: ")
    while message_list:
        current_message=message_list.pop()
        print(f"\t{current_message}.")
        sent_messages.append(current_message)


message_list=['this is sms one', 'this is sms two', 'this is sms three']
sent_messages=[]

show_messages(message_list[:])
send_messages(message_list[:], sent_messages)

print(f"Initial messages list is: {message_list}.")
print(f"Sent messages list is: {sent_messages}.")
