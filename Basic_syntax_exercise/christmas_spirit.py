quantity_of_decorations = int(input())
days_left_until_christmas = int(input())
ORNAMENT_SET_PRICE = 2
ORNAMENT_SET_POINTS = 5
TREE_SKIRT_PRICE = 5
TREE_SKIRT_POINTS = 3
TREE_GARLAND_PRICE = 3
TREE_GARLAND_POINTS = 10
TREE_LIGHTS_PRICE = 15
TREE_LIGHTS_POINTS = 17
total_price = 0
spirit_score = 0
for day_of_christmas in range(1, days_left_until_christmas + 1):
    if day_of_christmas % 11 == 0:
        quantity_of_decorations += 2
    if day_of_christmas % 2 == 0:
        total_price += ORNAMENT_SET_PRICE * quantity_of_decorations
        spirit_score += ORNAMENT_SET_POINTS
    if day_of_christmas % 3 == 0:
        total_price += TREE_SKIRT_PRICE * quantity_of_decorations + TREE_GARLAND_PRICE * quantity_of_decorations
        spirit_score += TREE_SKIRT_POINTS + TREE_GARLAND_POINTS
    if day_of_christmas % 5 == 0:
        total_price += TREE_LIGHTS_PRICE * quantity_of_decorations
        spirit_score += TREE_LIGHTS_POINTS
        if day_of_christmas % 3 == 0:
            spirit_score += 30
    if day_of_christmas % 10 == 0:
        spirit_score -= 20
        total_price += TREE_LIGHTS_PRICE + TREE_GARLAND_PRICE + TREE_SKIRT_PRICE
if days_left_until_christmas % 10 == 0:
    spirit_score -= 30
print(f"Total cost: {total_price}")
print(f"Total spirit: {spirit_score}")
