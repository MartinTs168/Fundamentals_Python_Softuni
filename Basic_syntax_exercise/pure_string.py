number_of_strings = int(input())
for _ in range(number_of_strings):
    string = input()
    for character in string:
        if character == '_' or character == '.' or character == ',':
            print(f"{string} is not pure!")
            break
    else:
        print(f"{string} is pure.")
