string = input()
farm = string.split(', ')
sheep_to_save = -1
for index in range(len(farm) - 1, -1, -1):
    if farm[index] == "wolf":
        if index == len(farm) - 1:
            print("Please go away and stop eating my sheep")
            break
        else:
            print(f"Oi! Sheep number {len(farm) - 1 - index}! You are about to be eaten by a wolf!")