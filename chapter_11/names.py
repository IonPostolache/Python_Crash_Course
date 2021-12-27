from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first1=input("\nPlease give me a first name: ")
    if first1=='q':
        break
    last1=input("\nPlease give me a last name: ")
    if last1=='q':
        break

    formatted_name=get_formatted_name(first1, last1)
    print(f"\tNeatly formatted name: {formatted_name}.")
