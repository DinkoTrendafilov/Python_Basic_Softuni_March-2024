number_of_breads = int(input())

best_baker_score = 0
best_baker_name = ''

for _ in range(number_of_breads):
    baker_name = input()
    current_baker_score = 0

    while True:
        command = input()
        if command == 'Stop':
            print(f"{baker_name} has {current_baker_score} points.")
            break
        points = command
        current_baker_score += int(points)

    if current_baker_score > best_baker_score:
        best_baker_name = baker_name
        best_baker_score = current_baker_score
        print(f"{baker_name} is the new number 1!")


print(f"{best_baker_name} won competition with {best_baker_score} points!")