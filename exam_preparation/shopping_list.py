shopping_list = input().split('!')
command = input()
while command != "Go Shopping!":
    command_type = command.split()[0]
    item = command.split()[1]
    if command_type == "Urgent":
        if item not in shopping_list:
            shopping_list.insert(0, item)
    elif item in shopping_list:
        if command_type == "Unnecessary":
            shopping_list.remove(item)
        elif command_type == "Correct":
            new_item = command.split()[2]
            index_of_old_item = shopping_list.index(item)
            shopping_list[index_of_old_item] = new_item
        elif command_type == "Rearrange":
            index_of_item = shopping_list.index(item)
            shopping_list.pop(index_of_item)
            shopping_list.append(item)

    command = input()
print(", ".join(shopping_list))
