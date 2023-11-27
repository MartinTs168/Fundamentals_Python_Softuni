import re

text = input()
pattern = r"([#|])+([a-zA-Z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"
result = re.findall(pattern, text)
total_calories = sum([int(match[3]) for match in result])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for element in result:
    print(f"Item: {element[1]}, Best before: {element[2]}, Nutrition: {element[3]}")
