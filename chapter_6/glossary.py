glossary={
    'KEYWORD': 'A reserved word the meaning of which cannot be changed by the user.',
    'OPERATOR': 'A reserved symbol that indicates an action to be performed.',
    'OBJECT': 'An individual thing you can interact with.',
    'VALUE':'An OBJECT that represents a single, concrete thing.',
    'COLLECTION':'An OBJECT that groups together or contains other OBJECTs.',
    }

#print(glossary['KEYWORD'])
for word, meaning in glossary.items():
    print(f"\n{word}: {meaning}")
