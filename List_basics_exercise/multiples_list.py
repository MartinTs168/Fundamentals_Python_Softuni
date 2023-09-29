factor = int(input())
count = int(input())
numbers_list = []
number = 0
for _ in range(count):
    number += factor
    numbers_list.append(number)
print(numbers_list)