number_of_lines = int(input())
positive_numbers = []
negative_numbers = []
for _ in range(number_of_lines):
    number = int(input())
    if number < 0:
        negative_numbers.append(number)
    else:
        positive_numbers.append(number)
print(positive_numbers)
print(negative_numbers)
count_of_positives = len(positive_numbers)
print(f"Count of positives: {count_of_positives}")
sum_of_negative_numbers = sum(negative_numbers)
print(f"Sum of negatives: {sum_of_negative_numbers}")
