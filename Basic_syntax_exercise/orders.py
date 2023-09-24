number_of_orders = int(input())
total_price = 0
for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if not 0.01 <= price_per_capsule <= 100 or not 1 <= days <= 31 or not 1 <= capsules_needed_per_day <= 2000:
        continue
    price_of_this_order = days * capsules_needed_per_day * price_per_capsule
    print(f"The price for the coffee is: ${price_of_this_order:.2f}")
    total_price += price_of_this_order
print(f"Total: ${total_price:.2f}")