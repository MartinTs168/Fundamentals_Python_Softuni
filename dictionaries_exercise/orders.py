items = {}
order = input().split()
while order[0] != 'buy':
    product = order[0]
    price = float(order[1])
    quantity = int(order[2])
    if product not in items.keys():
        items[product] = {"price": price, "quantity": quantity}
    else:
        items[product].update({"price": price})
        items[product]["quantity"] += quantity
    order = input().split()
for product, price_quantity in items.items():
    current_price = price_quantity['price'] * price_quantity['quantity']
    print(f"{product} -> {current_price:.2f}")