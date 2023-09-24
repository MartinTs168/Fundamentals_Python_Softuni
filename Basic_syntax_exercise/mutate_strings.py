# some_string = "Hello"
# print(len(some_string))
# print(some_string[:3])
# print(some_string[::-1]) #prints backwards

first_string = input()
seconds_string = input()
last_printed_string = first_string
for character_index in range(len(first_string)):
    left_part = seconds_string[0:character_index + 1]
    right_part = first_string[character_index +1:]
    new_string = left_part + right_part
    if not new_string == last_printed_string:
        last_printed_string = new_string
        print(new_string)