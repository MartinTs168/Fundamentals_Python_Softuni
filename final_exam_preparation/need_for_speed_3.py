def execute_commands(commands_list):
    for current_command in commands_list:
        command_info = current_command.split(" : ")
        command_type = command_info[0]
        current_car = command_info[1]
        if command_type == "Drive":
            current_distance = int(command_info[2])
            fuel_needed = int(command_info[3])
            drive(current_car, current_distance, fuel_needed)
        elif command_type == "Refuel":
            fuel_to_refill = int(command_info[2])
            refuel(current_car, fuel_to_refill)
        elif command_type == "Revert":
            killometers_to_revert = int(command_info[2])
            revert(current_car, killometers_to_revert)


def drive(car, distance, fuel):
    if cars[car]["fuel"] < fuel:
        print("Not enough fuel to make that ride")
    else:
        cars[car]["mileage"] += distance
        cars[car]["fuel"] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
    if cars[car]["mileage"] > 100000:
        print(f"Time to sell the {car}!")
        cars.pop(car)


def refuel(car, fuel):
    old_fuel = cars[car]["fuel"]
    cars[car]["fuel"] += fuel
    if cars[car]["fuel"] > 75:
        cars[car]["fuel"] = 75
    fuel_gained = cars[car]["fuel"] - old_fuel
    print(f"{car} refueled with {fuel_gained} liters ")


def revert(car, kilometers):
    cars[car]["mileage"] -= kilometers
    if cars[car]["mileage"] < 10000:
        cars[car]["mileage"] = 10000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")


cars = {}
commands = []
num_cars = int(input())
for _ in range(num_cars):
    car_info = input().split("|")
    car_brand = car_info[0]
    mileage = int(car_info[1])
    car_fuel = int(car_info[2])
    cars[car_brand] = {"mileage": mileage, "fuel": car_fuel}
while True:
    command = input()
    if command == "Stop":
        break
    commands.append(command)
execute_commands(commands)
for car, car_details in cars.items():
    print(f"{car} -> Mileage: {car_details['mileage']} kms, Fuel in the tank: {car_details['fuel']} lt.")
