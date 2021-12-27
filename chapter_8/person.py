"""
def build_person(first_name, last_name):
    #Return dictionary
    person={'first':first_name, 'last':last_name}
    return person

musician=build_person('john', 'travolta')
print(musician)
"""

def build_person(first_name, last_name, age=None):
    """Return dictionary"""
    person={'first':first_name, 'last':last_name}
    if age:
        person['age']=age
    return person

musician=build_person('john', 'travolta', age=27)
print(musician)
