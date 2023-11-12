text = input()
result = ''
old_character = ''
for character in text:
    if not character == old_character:
        result += character
    old_character = character
print(result)