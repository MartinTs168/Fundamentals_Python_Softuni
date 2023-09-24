string = input()
string = string.lower()
count_of_instances = 0
for character in string:
    if string.__contains__("water"):
        count_of_instances += 1
        string = string.replace("water", "", 1)
    elif string.__contains__("sand"):
        count_of_instances += 1
        string = string.replace("sand", "", 1)
    elif string.__contains__("fish"):
        count_of_instances += 1
        string = string.replace("fish", "", 1)
    elif string.__contains__("sun"):
        count_of_instances += 1
        string = string.replace("sun", "", 1)
print(count_of_instances)