def print_models(unprinted_designs, completed_designs):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print(f"printing: {current_design}")
        completed_designs.append(current_design)

def show_completed_designs(completed_designs):
    print("Models printed:")
    for every_completed in completed_designs:
        print(every_completed)
