import re

sentence = input().split()
deciphered_sentence = []
for word in sentence:
    character_code = re.findall(r"\d+", word)[0]
    word = word.replace(character_code, chr(int(character_code)))
    if len(word) > 2:
        word = word[0] + word[-1] + word[2:-1] + word[1]
    deciphered_sentence.append(word)
print(" ".join(deciphered_sentence))
