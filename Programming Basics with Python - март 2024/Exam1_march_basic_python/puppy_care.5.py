food_in_kg = int(input())

food_in_grams = food_in_kg * 1000

while True:
    command = input()

    if command == "Adopted":
        break
    eat_in_grams = int(command)
    food_in_grams -= eat_in_grams

diff = abs(food_in_grams)

if food_in_grams >= 0:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
