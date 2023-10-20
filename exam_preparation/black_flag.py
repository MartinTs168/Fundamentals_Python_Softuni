days_of_plunder = int(input())
daily_plunder = int(input())
target_plunder = int(input())
current_plunder = 0

for day in range(1, days_of_plunder + 1):
    current_plunder += daily_plunder
    if day % 3 == 0:
        current_plunder += 0.5 * daily_plunder
    if day % 5 == 0:
        current_plunder -= 0.3 * current_plunder

if current_plunder >= target_plunder:
    print(f"Ahoy! {current_plunder:.2f} plunder gained.")
else:
    percentage_gained = (current_plunder / target_plunder) * 100
    print(f"Collected only {percentage_gained:.2f}% of the plunder.")
