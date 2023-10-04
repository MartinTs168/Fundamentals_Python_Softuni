line = [int(x) for x in input().split(', ')]
formatted_line = []
count_of_zeroes = 0
for number in line:
    if number == 0:
        count_of_zeroes += 1
    else:
        formatted_line.append(number)
for i in range(count_of_zeroes):
    formatted_line.append(0)
print(formatted_line)