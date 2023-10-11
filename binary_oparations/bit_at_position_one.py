def solve(number):
    shifted_number = number >> 1
    result = shifted_number & 1
    return result


print(solve(13))
