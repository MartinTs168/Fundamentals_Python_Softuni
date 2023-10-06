def perfect_number(number:int) -> str:
    sum_divisors = 0
    for divisor in range(1,number):
        if number % divisor == 0:
            sum_divisors += divisor
    if sum_divisors == number:
        return "We have a perfect number!"
    return "It's not so perfect."


num1 = int(input())
print(perfect_number(num1))