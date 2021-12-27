glossary={
    'KEYWORD': 'A reserved word the meaning of which cannot be changed by the user.',
    'OPERATOR': 'A reserved symbol that indicates an action to be performed.',
    'OBJECT': 'An individual thing you can interact with.',
    'VALUE':'An OBJECT that represents a single, concrete thing.',
    'COLLECTION':'An OBJECT that groups together or contains other OBJECTs.',
    'CALLABLE': 'An OBJECT that represents some action to perform',
    'NAME': 'Any word that is not a KEYWORD, and that is used as an alias',
    'EXPRESSION': 'Any composite form of one or more of the above',
    'STATEMENT':'Any single line of code that is composed of at least one',
    'BLOCK':'At least two STATEMENTs that are bound together',
    'MODULE':'A single Python .py file; it’s composed of some number',
    }

#print(glossary['KEYWORD'])

for word, meaning in glossary.items():
    print(f"\n{word}: {meaning}")
