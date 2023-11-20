import re

sentence = input()
regex = r"\b_([a-zA-Z0-9]+)\b"
matches = re.findall(regex, sentence)
print(','.join(matches))
