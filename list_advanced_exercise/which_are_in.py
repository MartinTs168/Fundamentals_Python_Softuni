first_sequence = input().split(', ')
second_sequence = input().split(', ')
result = []
for text in first_sequence:
    for word in second_sequence:
        if word.__contains__(text):
            result.append(text)
            break

print(result)