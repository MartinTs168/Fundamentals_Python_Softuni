numbers = list(map(int, input().split()))
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))
