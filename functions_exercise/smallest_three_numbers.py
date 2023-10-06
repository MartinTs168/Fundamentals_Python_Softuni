def smallest_of_three(a, b, c):
    min_of_three = 0
    if a < b and a < c:
        min_of_three = a
    elif b < c and b < a:
        min_of_three = b
    elif c < a and c < b:
        min_of_three = c
    return min_of_three


number1 = int(input())
number2 = int(input())
number3 = int(input())
smallest_number = smallest_of_three(number1, number2, number3)
print(smallest_number)
