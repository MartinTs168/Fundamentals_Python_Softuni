text = input()
char_dict = {}
for character in text.replace(' ', ''):
    if character in char_dict.keys():
        char_dict[character] += 1
    else:
        char_dict[character] = 1
for key, value in char_dict.items():
    print(f"{key} -> {value}")
