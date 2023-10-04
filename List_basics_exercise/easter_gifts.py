list_of_gifts = input().split(" ")
command = input()
while command != "No Money":
    command = command.split(" ")
    command_type = command[0]
    if command_type == "OutOfStock":
        gift = command[1]
        for current_gift in list_of_gifts:
            if current_gift == gift:
                index_of_current_gift = list_of_gifts.index(current_gift)
                # list_of_gifts.insert(index_of_current_gift, str(None))
                list_of_gifts[index_of_current_gift] = str(None)
    elif command_type == "Required":
        current_index = int(command[2])
        if 0 <= current_index < len(list_of_gifts):
            list_of_gifts[current_index] = command[1]
    elif command_type == "JustInCase":
        list_of_gifts[-1] = command[1]
    command = input()
print(" ".join(x for x in list_of_gifts if x != "None"))