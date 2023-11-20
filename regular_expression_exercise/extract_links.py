import re

regex = r"\bwww\.[a-zA-Z0-9\-]+(\.[a-z]+)+\b"
all_text = ''
text = input()
while text:
    all_text += "\n"+text
    text = input()
matches = re.finditer(regex, all_text)
for match_obj in matches:
    print(match_obj.group())

