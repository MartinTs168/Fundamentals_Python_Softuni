ticket_price = 150
markup = 0.4
items = input().split("|")
budget = int(input())
items_bought_prices = []
for item in items:
    item_details = item.split("->")
    item_type = item_details[0]
    item_price = float(item_details[1])
    if budget < item_price:
        continue
    elif item_type == "Clothes" and item_price <= 50:
        budget -= item_price
        items_bought_prices.append(item_price)
    elif item_type == "Shoes" and item_price <= 35:
        budget -= item_price
        items_bought_prices.append(item_price)
    elif item_type == "Accessories" and item_price <= 20.50:
        budget -= item_price
        items_bought_prices.append(item_price)
total_price_before_markup = sum(items_bought_prices)
items_sold_prices = []
for item_price in items_bought_prices:
    item_price = item_price + item_price * markup
    budget += item_price
    items_sold_prices.append(item_price)
total_price_after_markup = sum(items_sold_prices)
profit = total_price_after_markup - total_price_before_markup
for item_price in items_sold_prices:
    print(f"{item_price:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")