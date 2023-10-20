#import numpy as np

sequence = input().split()
moves = 0
command = input()

while command != "end":
    moves += 1
    index_1 = int(command.split()[0])
    index_2 = int(command.split()[1])
    if (index_1 < 0 or index_1 >= len(sequence)) or (index_2 < 0 or index_2 >= len(sequence)) or index_1 == index_2:
        middle = len(sequence) // 2
        item = f"-{moves}a"
        sequence.insert(middle, item)
        sequence.insert(middle + 1, item)
        print("Invalid input! Adding additional elements to the board")
    elif sequence[index_1] == sequence[index_2]:
        element_1 = sequence[index_1]
        element_2 = sequence[index_2]
        sequence.remove(element_1)
        sequence.remove(element_2)
        print(f"Congrats! You have found matching elements - {element_1}!")
    else:
        print("Try again!")
    if len(sequence) == 0:
        print(f"You have won in {moves} turns!")
        break
    command = input()
else:
    print("Sorry you lose :(")
    print(" ".join(sequence))
