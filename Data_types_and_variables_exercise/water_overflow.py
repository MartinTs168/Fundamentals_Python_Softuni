TANK_CAPACITY = 255
number_of_lines = int(input())
liters_in_tank = 0
for i in range(number_of_lines):
    liters_to_pour_in_tank = int(input())
    if liters_to_pour_in_tank > TANK_CAPACITY:
        print("Insufficient capacity!")
        continue
    TANK_CAPACITY -= liters_to_pour_in_tank
    liters_in_tank += liters_to_pour_in_tank
print(liters_in_tank)