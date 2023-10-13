def sort_numbers_in_lists(numbers):
    positive_numbers = []
    negative_numbers = []
    even_numbers = []
    odd_numbers = []
    for number in numbers:
        if number >= 0:
            positive_numbers.append(str(number))
        else:
            negative_numbers.append(str(number))
        if number % 2 == 0:
            even_numbers.append(str(number))
        else:
            odd_numbers.append(str(number))
    return ', '.join(positive_numbers), ', '.join(negative_numbers), ', '.join(even_numbers), ', '.join(odd_numbers)


numbers = list(map(int, input().split(', ')))
result = sort_numbers_in_lists(numbers)
print(f"Positive: {result[0]}")
print(f"Negative: {result[1]}")
print(f"Even: {result[2]}")
print(f"Odd: {result[3]}")
