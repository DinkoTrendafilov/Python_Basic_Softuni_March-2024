goal_meters = 8848
initial_meters = 5364
yes_days_counter = 0
days_counter = 0
is_achieve = False

while True:
    command = input()
    if command == "END":
        break
    day_meters = int(input())
    days_counter += 1
    if command == "Yes":
        yes_days_counter += 1
        if yes_days_counter >= 5:
            break

    initial_meters += day_meters
    if initial_meters >= goal_meters:
        is_achieve = True
        break

if is_achieve:
    print(f"Goal reached for {days_counter} days!")
else:
    print("Failed!")
    print(f"{initial_meters}")
