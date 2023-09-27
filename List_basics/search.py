number_of_lines = int(input())
word = input()
my_list = []

for _ in range(number_of_lines):
    text = input()
    my_list.append(text)
print(my_list)

filtered_list = []

for current_text in my_list:
    if word in current_text:
        filtered_list.append(current_text)
print(filtered_list)
