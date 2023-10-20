def check_index_validation(index_1, status):
    if 0 <= index_1 < len(status):
        return True
    else:
        return False


def check_index_validation_2(index_1, index_2, status) -> bool:
    if 0 <= index_1 < len(status) and 0 <= index_2 < len(status):
        return True
    else:
        return False


def is_section_broken(section):
    if section <= 0:
        return True
    else:
        return False


pirate_ship_status = list(map(int, input().split('>')))
warship_status = list(map(int, input().split('>')))
section_max_health = int(input())
command = input()
while command != "Retire":
    command_info = command.split()
    command_type = command_info[0]
    if command_type == "Fire":
        index = int(command_info[1])
        damage = int(command_info[2])
        if check_index_validation(index, warship_status):
            warship_status[index] -= damage
            if is_section_broken(warship_status[index]):
                print("You won the enemy ship has sunken.")
                break
    elif command_type == "Defend":
        start_index = int(command_info[1])
        end_index = int(command_info[2])
        damage = int(command_info[3])
        sunk = False
        if check_index_validation_2(start_index, end_index, pirate_ship_status):
            for index in range(start_index, end_index + 1):
                pirate_ship_status[index] -= damage
                if is_section_broken(pirate_ship_status[index]):
                    print("You lost! The pirate ship has sunken.")
                    sunk = True
                    break
            if sunk:
                break
    elif command_type == "Repair":
        index = int(command_info[1])
        health = int(command_info[2])
        if check_index_validation(index, pirate_ship_status):
            pirate_ship_status[index] = min(pirate_ship_status[index] + health, section_max_health)
    elif command_type == "Status":
        section_for_repair = sum(1 for section in pirate_ship_status if section < 0.2 * section_max_health)
        print(f"{section_for_repair} sections need repair.")
    command = input()
else:
    pirate_ship_total_status = sum(pirate_ship_status)
    warship_total_status = sum(warship_status)
    print(f"Pirate ship status: {pirate_ship_total_status}")
    print(f"Warship status: {warship_total_status}")
