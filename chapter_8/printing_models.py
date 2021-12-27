unprinted_designs=['phone', 'case', 'box']
completed_designs=[]

while unprinted_designs:
    current_design=unprinted_designs.pop()
    print(f"printing: {current_design}")
    completed_designs.append(current_design)


print("Models printed:")
for every_completed in completed_designs:
    print(every_completed)

print(f"Unprinted designs: {unprinted_designs}.")
