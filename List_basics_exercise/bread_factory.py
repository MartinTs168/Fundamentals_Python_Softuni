initial_energy = 100
initial_coins = 100
events = input().split("|")

for event in events:
    event_items = event.split("-")
    event_type = event_items[0]
    event_value = event_items[1]
    if event_type == "rest":
        current_energy = initial_energy
        initial_energy += int(event_value)
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")
    elif event_type == "order":
        if initial_energy >= 30:
            print(f"You earned {event_value} coins.")
            initial_energy -= 30
            initial_coins += int(event_value)
        else:
            initial_energy += 50
            print("You had to rest!")
    else:
        if initial_coins >= int(event_value):
            initial_coins -= int(event_value)
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")