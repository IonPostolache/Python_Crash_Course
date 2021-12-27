stanior={'first_name':'tanior', 'last_name':'selim', 'age':38, 'city':'galati'}
#print(stanior['first'].title())
#print(stanior['last'].title())
#print(stanior['age'])
#print(stanior['city'].title())

aonciu={'first_name': 'adrian', 'last_name':'onciu', 'age': 35, 'city':'untesti'}

gcudalb={'first_name':'george', 'last_name':'cudalb', 'age': 34, 'city': 'tulcea'}

people=[stanior, aonciu, gcudalb]

for every_people in people:
    #print(every_people)
    for a, b, in every_people.items():
        if type(b)==str:
            print(f"{a.title()} is: {b.title()}")
        elif type(b)==int:
            print(f"{a.title()} is: {b}")
        #print(type(b))
    print("\n")
