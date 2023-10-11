def solve(number, position):
    shifted_number = number >> position
    return shifted_number & 1


print(solve(2145,5))