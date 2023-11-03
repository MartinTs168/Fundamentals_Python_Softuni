command = input()
products = {}
while command != "statistics":
    info = command.split(': ')
    key = info[0]
    value = info[1]
    if key in products:
        products[key] += int(value)
    else:
        products[key] = int(value)
    command = input()
print("Products in stock:")
for product,quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")