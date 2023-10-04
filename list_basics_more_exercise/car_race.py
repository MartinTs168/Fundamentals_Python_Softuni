sequence_of_numbers = [int(x) for x in input().split(' ')]
middle = len(sequence_of_numbers) // 2
left_side = sequence_of_numbers[:middle]
right_side = sequence_of_numbers[middle + 1:]
left_racer_time = 0
right_racer_time = 0
for i in range(len(left_side)):
    seconds = left_side[i]
    if seconds == 0:
        left_racer_time -= left_racer_time * 0.2
    else:
        left_racer_time += seconds
for j in range(len(right_side) - 1, -1, -1):
    seconds = right_side[j]
    if seconds == 0:
        right_racer_time -= right_racer_time * 0.2
    else:
        right_racer_time += seconds
if left_racer_time < right_racer_time:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_time:.1f}")