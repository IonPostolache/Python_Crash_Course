import printing_functions


unprinted_designs=['phone', 'case', 'box']
completed_designs=[]

printing_functions.print_models(unprinted_designs[:], completed_designs)
printing_functions.show_completed_designs(completed_designs)

print(f"Unprinted designs: {unprinted_designs}.")
