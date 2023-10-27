class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        string_to_print = ''
        if species == 'mammal':
            string_to_print += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}"
        elif species == 'fish':
            string_to_print += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}"
        elif species == 'bird':
            string_to_print += f"Birds in {self.zoo_name}: {', '.join(self.birds)}"
        string_to_print += f"\nTotal animals: {Zoo.__animals}"
        return string_to_print


name_of_zoo = input()
zoo = Zoo(name_of_zoo)
number_of_lines = int(input())
for i in range(number_of_lines):
    animal_species, animal_name = input().split()
    zoo.add_animal(animal_species, animal_name)
species = input()
print(zoo.get_info(species))
