def solve(number, digit):
    count = 0
    while number > 0:
        remainder = number % 2
        number = number // 2
        if remainder == digit:
            count += 1
    return count


print(solve(20, 0))
