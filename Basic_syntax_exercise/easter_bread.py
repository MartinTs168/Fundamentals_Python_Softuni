budget = float(input())
flour_price_1kg = float(input())
pack_of_eggs_price = flour_price_1kg * 0.75
milk_price_1L = flour_price_1kg * 1.25
price_to_cook_one_bread = flour_price_1kg + pack_of_eggs_price + (milk_price_1L / 4)
number_of_loaves_baked = 0
colored_eggs_count = 0
while budget >= price_to_cook_one_bread:
    number_of_loaves_baked += 1
    budget -= price_to_cook_one_bread
    colored_eggs_count += 3
    if number_of_loaves_baked % 3 == 0:
        colored_eggs_count -= number_of_loaves_baked - 2
print(f"You made {number_of_loaves_baked} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")
