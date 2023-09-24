number_of_lines = int(input())
balanced = False
previous_line = ""
for i in range(number_of_lines):
    line = input()
    if line == "(":
        if previous_line == "(":
            balanced = False
            break
        previous_line = line
    elif line == ")":
        if previous_line == "(":
            previous_line = line
            balanced = True
        else:
            balanced = False
            break
if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
