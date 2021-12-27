def sandwich(*salads):
    """This function will take any number of arguments."""
    print(f"Making a sandwich with: ")
    for salad in salads:
        print(f"\t{salad.title()}.")
