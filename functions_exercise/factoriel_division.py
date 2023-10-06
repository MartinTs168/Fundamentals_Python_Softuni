def calculate_factorial(number: int) -> int:
    for current_number in range(1, number):
        number *= current_number
    return number


first_number = int(input())
second_number = int(input())
result = calculate_factorial(first_number) / calculate_factorial(second_number)
print(f"{result:.2f}")
