player_name = input()

initial_points = 301
successful_attempts = 0
unsuccessful_attempts = 0

while True:
    command = input()
    if command == 'Retire':
        break
    points = int(input())
    if command == 'Double':
        points *= 2
    elif command == 'Triple':
        points *= 3
    if points > initial_points:
        unsuccessful_attempts += 1
    else:
        successful_attempts += 1
        initial_points -= points
    if initial_points == 0:
        break

if initial_points == 0:
    print(f"{player_name} won the leg with {successful_attempts} shots.")
else:
    print(f"{player_name} retired after {unsuccessful_attempts} unsuccessful shots.")
