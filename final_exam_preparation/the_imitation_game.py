encrypted_message = input()
while True:
    command = input().split('|')
    if command[0] == "Decode":
        break
    command_type = command[0]
    if command_type == "Move":
        number_of_letters = int(command[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]
    elif command_type == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif command_type == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
print(f"The decrypted message is: {encrypted_message}")

