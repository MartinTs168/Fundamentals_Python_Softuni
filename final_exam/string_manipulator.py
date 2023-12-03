text = input()
while True:
    command = input().split()
    if command[0] == "End":
        break
    elif command[0] == "Translate":
        char = command[1]
        replacement = command[2]
        text = text.replace(char, replacement)
        print(text)
    elif command[0] == "Includes":
        substring = command[1]
        if substring in text:
            print("True")
        else:
            print("False")
    elif command[0] == "Start":
        substring = command[1]
        if text.startswith(substring):
            print("True")
        else:
            print("False")
    elif command[0] == "Lowercase":
        text = text.lower()
        print(text)
    elif command[0] == "FindIndex":
        char = command[1]
        print(text.rfind(char))
    elif command[0] == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        text = text[0:start_index] + text[start_index + count:]
        print(text)