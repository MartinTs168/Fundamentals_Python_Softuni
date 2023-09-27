animal = []
for _ in range(3):
    animal.append(input())

animal[0], animal[2] = animal[2], animal[0]
print(animal)