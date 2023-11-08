resources = {}
counter = 0
last_line = ''
while True:
    counter += 1
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource not in resources.keys():
        resources[resource] = quantity
    else:
        resources[resource] += quantity
for key, value in resources.items():
    print(f"{key} -> {value}")
