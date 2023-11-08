garage = {}
num_lines = int(input())
for _ in range(num_lines):
    command = input().split()
    command_type = command[0]
    name = command[1]
    if command_type == 'register':
        licence_number = command[2]
        if name in garage.keys():
            print(f"ERROR: already registered with plate number {garage[name]}")
        else:
            garage[name] = licence_number
            print(f"{name} registered {licence_number} successfully")
    elif command_type == 'unregister':
        if name not in garage.keys():
            print(f"ERROR: user {name} not found")
        else:
            del garage[name]
            print(f"{name} unregistered successfully")
for driver, licence in garage.items():
    print(f"{driver} => {licence}")

