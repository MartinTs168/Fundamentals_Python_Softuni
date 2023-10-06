def sum_odd_and_even_chars(number_str: str):
    even_sum = 0
    odd_sum = 0
    for digit in number_str:
        digit_as_int = int(digit)
        if digit_as_int % 2 == 0:
            even_sum += digit_as_int
        elif digit_as_int % 2 != 0:
            odd_sum += digit_as_int
    return odd_sum, even_sum


number = input()
result = sum_odd_and_even_chars(number)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")