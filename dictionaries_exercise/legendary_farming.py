inventory = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
legendary_item = ''
obtained = False
while not obtained:
    current_items = input().split()
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in inventory.keys():
            if key not in junk.keys():
                junk[key] = value
            else:
                junk[key] += value
        else:
            inventory[key] += value
        if inventory['shards'] >= 250:
            legendary_item = 'Shadowmourne'
            inventory['shards'] -= 250
            obtained = True
            break
        elif inventory['fragments'] >= 250:
            legendary_item = 'Valanyr'
            inventory['fragments'] -= 250
            obtained = True
            break
        elif inventory['motes'] >= 250:
            legendary_item = 'Dragonwrath'
            inventory['motes'] -= 250
            obtained = True
            break
print(f"{legendary_item} obtained!")
print(f"shards: {inventory['shards']}")
print(f"fragments: {inventory['fragments']}")
print(f"motes: {inventory['motes']}")
for item, amount in junk.items():
    print(f"{item}: {amount}")
