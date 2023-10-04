sequence = input().split(" ")
text = input()
message = ""
for number in sequence:
    sum_number = 0
    for _, char_number in enumerate(number):
        sum_number += int(char_number)
    number_of_times_length_of_text_in_sum_number = sum_number // len(text)
    sum_number -= len(text) * number_of_times_length_of_text_in_sum_number
    index = sum_number - len(text)
    message += text[index]
    text = text[:index] + text[index + 1:]
print(message)
