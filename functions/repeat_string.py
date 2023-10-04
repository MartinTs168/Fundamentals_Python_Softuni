string = input()
n = int(input())
repeat_string = lambda a, b: a * b
repeated_string = repeat_string(string, n)
print(repeated_string)
