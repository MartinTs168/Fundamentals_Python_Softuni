# year = int(input())
# while True:
#     year += 1
#     year_string = str(year)
#     digits = []
#     for digit in year_string:
#         if digits.__contains__(digit):
#             break
#         digits.append(digit)
#     else:
#         print(year_string)
#         break

year = int(input())
while True:
    year += 1
    year_as_string = str(year)
    if len(year_as_string) == len(set(year_as_string)): # set gives only the unique elements so the length changes
        break
print(year_as_string)
