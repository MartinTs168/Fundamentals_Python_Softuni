import sys

snowballs_made = int(input())
highest_value_snowball = -sys.maxsize
max_weight = 0
max_time = 0
max_quality = 0
for snowball in range(snowballs_made):
    snowball_weight = int(input())
    time_needed_to_hit_target = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight / time_needed_to_hit_target) ** snowball_quality
    if snowball_value > highest_value_snowball:
        highest_value_snowball = int(snowball_value)
        max_weight = snowball_weight
        max_time = time_needed_to_hit_target
        max_quality = snowball_quality
print(f"{max_weight} : {max_time} = {highest_value_snowball} ({max_quality})")