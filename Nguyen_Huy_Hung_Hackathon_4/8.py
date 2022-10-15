import random as r
skills = [
    {
        "Name": "Tackle",
        "Minimum Level": 1,
        "Damage": 5,
        "Hit Rate": 0.3
    },
    {
        "Name": "Quick Attack",
        "Minimum Level": 2,
        "Damage": 3,
        "Hit Rate": 0.5
    },
    {
        "Name": "Strong Kick",
        "Minimum Level": 4,
        "Damage": 9,
        "Hit Rate": 0.2
    }
]

character = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': ['Shield', 'Bread Loaf', 'Flintstone'],
    'Gold': 100,
    'Level': 2
}
def backpackItems():
    print()
    print("Items to level up:")
    for i in range(len(character['Backpack'])):
        print("- ", end='')
        print(character['Backpack'][i])

def levelUp(inp: str):
    if inp == character['Backpack'][1]:
        character["Level"] += 1
        print('\nLeveled Up!')
    else:
        print('Cannot level up with this item.')

rate = r.random()
def gameOn():
    print()
    for i in range(len(skills)):
        print(f'''Skill {i+1}: {skills[i]['Name']}''')
    inp = int(input('Choose skill by number: '))
    print(f'''You chose {skills[inp-1]["Name"]}''')

    if character["Level"] >= skills[inp-1]["Minimum Level"]:
        if rate <= skills[inp-1]["Hit Rate"]:
            print(f"""Damage: {skills[inp-1]["Damage"]}""")
        else:
            print("missed lol n00b")
    else:
        print(f"""Cannot deploy. Required level {skills[inp-1]["Minimum Level"]}""")
        print()
        print(f"""Level of main character: {character["Level"]}""")
        backpackItems()
        levelUp(input("Select item: "))
        gameOn()

gameOn()