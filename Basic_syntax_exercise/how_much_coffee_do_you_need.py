command = input()
cups_needed = 0

while command != "END":
    upper_case_or_not = command.isupper()
    command = command.lower()
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        if upper_case_or_not:
            cups_needed += 2
        else:
            cups_needed += 1
        if cups_needed > 5:
            print("You need extra sleep")
            break
    command = input()
else:
    print(cups_needed)
