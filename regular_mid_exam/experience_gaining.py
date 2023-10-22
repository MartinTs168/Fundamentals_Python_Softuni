exp_to_unlock_tank = float(input())
number_of_battles = int(input())
total_exp = 0
for battle in range(1, number_of_battles + 1):
    exp_gained = float(input())
    total_exp += exp_gained
    if battle % 3 == 0:
        total_exp += 0.15 * exp_gained
    if battle % 5 == 0:
        total_exp -= 0.1 * exp_gained
    if battle % 15 == 0:
        total_exp += 0.5 * exp_gained
    if total_exp >= exp_to_unlock_tank:
        print(f"Player successfully collected his needed experience for {battle} battles.")
        break
else:
    remaining_exp = exp_to_unlock_tank - total_exp
    print(f"Player was not able to collect the needed experience, {remaining_exp:.2f} more needed.")
