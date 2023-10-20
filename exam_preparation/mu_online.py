health = 100
bitcoins = 0
rooms = input().split('|')
room_number = 0
for room in rooms:
    room_number += 1
    room_info = room.split()
    command = room_info[0]
    if command == 'potion':
        heal = int(room_info[1])
        old_health = health
        health += heal
        if health > 100:
            health = 100
        health_gained = health - old_health
        print(f"You healed for {health_gained} hp.")
        print(f"Current health: {health} hp.")
    elif command == 'chest':
        bitcoins_found = int(room_info[1])
        print(f"You found {bitcoins_found} bitcoins.")
        bitcoins += bitcoins_found
    else:
        monster = command
        monster_attack = int(room_info[1])
        health -= monster_attack
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room_number}")
            break
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
