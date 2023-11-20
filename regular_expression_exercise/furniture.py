import re

pattern = r">>(\w+)<<(\d+\.?\d*)!(\d+)"
bought_furniture = []
total_price = 0
while True:
    current_furniture = input()
    if current_furniture == 'Purchase':
        break
    match = re.search(pattern, current_furniture)
    if match is not None:
        furniture_type = match.group(1)
        price = float(match.group(2))
        quantity = int(match.group(3))
        total_price += price * quantity
        bought_furniture.append(furniture_type)
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_price:.2f}")
