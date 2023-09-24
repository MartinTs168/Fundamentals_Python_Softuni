name = input()
while not name == "Welcome!":
    house = ""
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    if len(name) < 5:
        house = "Gryffindor"
    elif len(name) == 5:
        house = "Slytherin"
    elif len(name) == 6:
        house = "Ravenclaw"
    else:
        house = "Hufflepuff"
    print(f"{name} goes to {house}.")
    name = input()
else:
    print("Welcome to Hogwarts.")