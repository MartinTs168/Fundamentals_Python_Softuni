current_version = list(map(int, input().split('.')))
# current_version[2] += 1
# if current_version[2] == 10:
#     current_version[2] = 0
#     current_version[1] += 1
#     if current_version[1] == 10:
#         current_version[1] = 0
#         current_version[0] += 1
# future_version = list(map(str, current_version))
# print('.'.join(future_version))

number = int(''.join(str(i) for i in current_version))
number += 1
print('.'.join(str(number)))