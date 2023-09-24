number = int(input())
for current_number in range(1, number + 1):
    message = ""
    sum_of_digits = 0
    current_number_string = str(current_number)
    for digit in current_number_string:
        sum_of_digits += int(digit)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        message = "True"
    else:
        message = "False"
    print(f"{current_number} -> {message}")