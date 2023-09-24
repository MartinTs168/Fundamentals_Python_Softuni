number = input()
largest_number = ""
largest_digit = 0
index_of_largest_digit = -1
for _ in range(len(number)):
    current_index = 0
    largest_digit = 0
    index_of_largest_digit = -1
    for next_index in range(current_index, len(number)):
        if int(number[next_index]) > largest_digit:
            largest_digit = int(number[next_index])
            index_of_largest_digit = next_index
    largest_number += str(largest_digit)
    number = number[:index_of_largest_digit] + number[index_of_largest_digit + 1:]
print(largest_number)
