def sandwich(*salads):
    print(f"Making a sandwich with: ")
    for salad in salads:
        print(f"\t{salad.title()}.")


sandwich('salami', 'mustard')
sandwich('burger', 'ketchup', 'salad')
sandwich('chicken', 'bbq sauce', 'chips', 'pepsi')
