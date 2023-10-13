number_of_electrons = int(input())
shells = []
for current_shell in range(1, number_of_electrons + 1):
    max_shell_capacity = 2 * current_shell ** 2
    if number_of_electrons >= max_shell_capacity:
        shells.append(max_shell_capacity)
        number_of_electrons -= max_shell_capacity
    else:
        shells.append(number_of_electrons)
        break
    if number_of_electrons <= 0:
        break
print(shells)


