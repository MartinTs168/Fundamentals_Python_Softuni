def get_total_price(product: str, number_of_products: int) -> float:
    price = 0
    if product == "water":
        price = 1
    elif product == "coffee":
        price = 1.5
    elif product == "coke":
        price = 1.4
    elif product == "snacks":
        price = 2
    return price * number_of_products


product = input()
number_of_products = int(input())
total_price = get_total_price(product, number_of_products)
print(f"{total_price:.2f}")