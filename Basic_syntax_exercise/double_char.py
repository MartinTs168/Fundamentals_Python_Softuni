string = input()
while not string == "End":
    if not string == "SoftUni":
        new_string = ""
        for character in string:
            new_string += character * 2
        print(new_string)
    string = input()