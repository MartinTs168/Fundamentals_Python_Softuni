spell_book = {}
while True:
    command = input().split()
    if command[0] == "End":
        break
    elif command[0] == "Enroll":
        hero_name = command[1]
        if hero_name not in spell_book.keys():
            spell_book[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")
    elif command[0] == "Learn":
        hero_name = command[1]
        spell = command[2]
        if hero_name not in spell_book.keys():
            print(f"{hero_name} doesn't exist.")
        elif spell in spell_book[hero_name]:
            print(f"{hero_name} has already learnt {spell}.")
        else:
            spell_book[hero_name].append(spell)
    elif command[0] == "Unlearn":
        hero_name = command[1]
        spell = command[2]
        if hero_name not in spell_book.keys():
            print(f"{hero_name} doesn't exist.")
        elif spell not in spell_book[hero_name]:
            print(f"{hero_name} doesn't know {spell}.")
        else:
            spell_book[hero_name].pop(spell_book[hero_name].index(spell))
print("Heroes:")
for hero, spells in spell_book.items():
    print(f"== {hero}: {', '.join(spells)}")