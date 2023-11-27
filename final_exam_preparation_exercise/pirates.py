cities = {}
while True:
    city_info = input().split('||')
    if city_info[0] == 'Sail':
        break
    city_name = city_info[0]
    population = int(city_info[1])
    gold = int(city_info[2])
    if city_name not in cities.keys():
        cities[city_name] = {"population": population, "gold": gold}
    else:
        cities[city_name]["population"] += population
        cities[city_name]["gold"] += gold
while True:
    event_info = input().split('=>')
    if event_info[0] == 'End':
        break
    town = event_info[1]
    if event_info[0] == 'Plunder':
        people_killed = int(event_info[2])
        gold_stolen = int(event_info[3])
        cities[town]["population"] -= people_killed
        cities[town]["gold"] -= gold_stolen
        print(f"{town} plundered! {gold_stolen} gold stolen, {people_killed} citizens killed.")
        if cities[town]["gold"] == 0 or cities[town]["population"] == 0:
            print(f"{town} has been wiped off the map!")
            del cities[town]
    elif event_info[0] == "Prosper":
        gold_gained = int(event_info[2])
        if gold_gained < 0:
            print("Gold added cannot be a negative number!")
            continue
        cities[town]["gold"] += gold_gained
        print(f"{gold_gained} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
if len(cities) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town_name, city_details in cities.items():
        print(f"{town_name} -> Population: {city_details['population']} citizens, Gold: {city_details['gold']} kg")


