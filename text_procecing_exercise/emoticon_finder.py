text = input()
emojis = ''
for index in range(len(text)):
    symbol = text[index]
    if symbol == ':':
        emojis += symbol + text[index + 1] + '\n'
print(emojis)
