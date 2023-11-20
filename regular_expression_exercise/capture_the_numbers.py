import re

regex = r"\d+"
all_text = ''
text = input()
while text:
    all_text += text
    text = input()
matches = re.findall(regex, all_text)
print(' '.join(matches))