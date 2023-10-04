effort = 0
total_fire_put_out = 0
fire = input().split("#")
water = int(input())
cells_put_out = []
for i in range(len(fire)):
    fire_details = fire[i].split(" = ")
    fire_type = fire_details[0]
    value_of_cell = int(fire_details[1])
    if water < value_of_cell:
        continue
    elif fire_type == "High" and (81 <= value_of_cell <= 125):
        water -= value_of_cell
        total_fire_put_out += value_of_cell
        effort += value_of_cell / 4
    elif fire_type == "Medium" and (51 <= value_of_cell <= 80):
        water -= value_of_cell
        total_fire_put_out += value_of_cell
        effort += value_of_cell / 4
    elif fire_type == "Low" and (1 <= value_of_cell <= 50):
        water -= value_of_cell
        total_fire_put_out += value_of_cell
        effort += value_of_cell / 4
    else:
        continue
    cells_put_out.append(value_of_cell)
print("Cells:")
for cell in cells_put_out:
    print(f"- {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire_put_out}")