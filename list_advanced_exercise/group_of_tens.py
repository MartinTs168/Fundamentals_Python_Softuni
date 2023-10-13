from math import ceil
numbers = list(map(int, input().split(', ')))
max_number = max(numbers)
for current_group in range(1, (ceil(max_number / 10)) + 1):
    group = list(filter(lambda x: x <= current_group * 10, numbers))
    numbers = [number for number in numbers if number not in group]
    print(f"Group of {current_group * 10}'s: {group}")
