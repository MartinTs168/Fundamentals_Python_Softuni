def sum_numbers(number1, number2):
    return number1 + number2


def subtract_numbers(result, number3):
    return result - number3


def sum_and_subtract(number_1, number_2, number_3):
    sum_of_two = sum_numbers(number_1, number_2)
    return subtract_numbers(sum_of_two, number_3)


num1 = int(input())
num2 = int(input())
num3 = int(input())
result_ = sum_and_subtract(num1, num2, num3)
print(result_)
