numbers = [int(x) for x in input().split(' ')]
count_of_numbers_to_remove = int(input())
sorted_numbers = sorted(numbers,reverse=False)
for i in range(count_of_numbers_to_remove):
    sorted_numbers.pop(0)
string_numbers = [str(i) for i in numbers if i in sorted_numbers]
print(", ".join(string_numbers))
