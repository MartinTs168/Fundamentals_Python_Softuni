import re

pattern = r"(?<!\W|[a-z0-9A-Z])([$%])([A-Z][a-z]{2,})\1:\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|(?!\W|[0-9a-zA-z])"
number_of_messages = int(input())
for _ in range(number_of_messages):
    current_message = input()
    match = re.search(pattern, current_message)
    if match:
        first_letter = chr(int(match.group(3)))
        second_letter = chr(int(match.group(4)))
        third_letter = chr(int(match.group(5)))
        decrypted_message = first_letter + second_letter + third_letter
        print(f"{match.group(2)}: {decrypted_message}")
    else:
        print("Valid message not found!")
