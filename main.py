#Make 3 dictionaries where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner's name.
#Store these dictionaries in a list called "pets".
#Next, loop through your list and as you do, print everything you know about each pet. Make sure the final output is nicely formatted and neat.
dic1={
'animal':'dog',
'owner':'Adelio',
}

dic2={
'animal':'cat',
'owner':'Bob',
}
    
dic3={
    'animal':'fish',
    'owner':'Simon'
}

pets=[dic1,dic2,dic3]
counter=1
for pet in pets:
    print('')
    print(f'animal number {counter} informations:')
    counter+=1
    print(f'kind of animal: {pet['animal']}')
    print(f"owner's name: {pet['owner']}")