import re

sentence = input()
regex = input()
regex = rf"\b{regex}\b"
matches = re.findall(regex, sentence, re.IGNORECASE)
print(len(matches))