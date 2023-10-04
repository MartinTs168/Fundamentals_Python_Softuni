line_of_numbers = input().split(' ')
numbers = []
for number in line_of_numbers:
    numbers.append(abs(float(number)))
print(numbers)