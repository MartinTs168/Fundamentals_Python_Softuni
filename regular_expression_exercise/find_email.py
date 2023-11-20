import re

sentence = input()
pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
extracted_email = re.findall(pattern, sentence)
for email in extracted_email:
    print(email[0])