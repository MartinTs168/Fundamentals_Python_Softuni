starting_number = int(input())
ending_number = int(input())
for ascii_number in range(starting_number, ending_number + 1):
    if ascii_number == ending_number:
        print(chr(ascii_number))
    else:
        print(chr(ascii_number), end=" ")