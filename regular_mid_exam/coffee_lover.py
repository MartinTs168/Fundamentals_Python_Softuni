coffee_list = input().split()
number_of_commands = int(input())
for _ in range(number_of_commands):
    command = input().split()
    command_type = command[0]
    if command_type == 'Include':
        coffee = command[1]
        coffee_list.append(coffee)
    elif command_type == 'Remove':
        number_of_coffees = int(command[2])
        if number_of_coffees <= len(coffee_list):
            first_or_last = command[1]
            if first_or_last == 'first':
                for i in range(number_of_coffees):
                    coffee_list.pop(0)
            elif first_or_last == 'last':
                for i in range(number_of_coffees):
                    coffee_list.pop()
    elif command_type == 'Prefer':
        index_1 = int(command[1])
        index_2 = int(command[2])
        if 0 <= index_1 < len(coffee_list) and 0 <= index_2 < len(coffee_list):
            coffee = coffee_list[index_1]
            coffee_list[index_1] = coffee_list[index_2]
            coffee_list[index_2] = coffee
    elif command_type == 'Reverse':
        coffee_list.reverse()
print("Coffees:")
print(" ".join(coffee_list))