chat = []
while True:
    command = input().split()
    command_type = command[0]
    if command_type == "end":
        break
    elif command_type == "Chat":
        message = command[1]
        chat.append(message)
    elif command_type == "Delete":
        message = command[1]
        if message in chat:
            chat.remove(message)
    elif command_type == "Edit":
        message = command[1]
        edited_message = command[2]
        if message in chat:
            index_of_message = chat.index(message)
            chat[index_of_message] = edited_message
    elif command_type == "Pin":
        message = command[1]
        if message in chat:
            chat.remove(message)
            chat.append(message)
    elif command_type == "Spam":
        messages = command[1:]
        for message in messages:
            chat.append(message)
print("\n".join(chat))