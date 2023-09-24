word = input()
indexes_of_capital_letters = []
for index, character in enumerate(word):
    if character.isupper():
        indexes_of_capital_letters.append(index)
print(indexes_of_capital_letters)