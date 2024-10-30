number_sea_relax = int(input())
number_mountain_relax = int(input())

profit = 0

while True:
    command = input()
    if command == "Stop":
        break

    packed_name = command
    if packed_name == "sea":
        if number_sea_relax <= 0:
            continue
        number_sea_relax -= 1
        profit += 680
    elif packed_name == "mountain":
        if number_mountain_relax <= 0:
            continue
        number_mountain_relax -= 1
        profit += 499

    if number_sea_relax == 0 and number_mountain_relax == 0:
        break

if number_sea_relax == 0 and number_mountain_relax == 0:
    print(" Good job! Everything is sold.")

print(f"Profit: {profit:} leva.")
