def show_messages(message_list):
    print("These are the messages: ")
    for every_message in message_list:
        print(f"\t{every_message.title()}.")


message_list=['this is sms one', 'this is sms two', 'this is sms three']

show_messages(message_list)
