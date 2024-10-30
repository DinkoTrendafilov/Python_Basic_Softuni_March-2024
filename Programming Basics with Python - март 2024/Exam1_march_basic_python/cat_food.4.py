number_of_cats = int(input())

price_cat_food_per_kg = 12.45
total_food_in_grams = 0
numer_of_small_cats = 0
numer_of_big_cats = 0
numer_of_huge_cats = 0

for _ in range(number_of_cats):
    current_food_in_grams = float(input())
    total_food_in_grams += current_food_in_grams

    if 100 <= current_food_in_grams < 200:
        numer_of_small_cats += 1
    elif 200 <= current_food_in_grams < 300:
        numer_of_big_cats += 1
    elif 300 <= current_food_in_grams < 400:
        numer_of_huge_cats += 1

price_food = total_food_in_grams / 1000 * price_cat_food_per_kg

print(f"Group 1: {numer_of_small_cats} cats.")
print(f"Group 2: {numer_of_big_cats} cats.")
print(f"Group 3: {numer_of_huge_cats} cats.")
print(f"Price for food per day: {price_food:.2f} lv.")
