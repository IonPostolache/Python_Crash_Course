favorite_places={'ben':['austria'], 'andy':['tesco'], 'kiran':['kerala', 'church']}

for k, v in favorite_places.items():
    print(f"{k.title()}:")
    for place in v:
        print(f"-{place}")
