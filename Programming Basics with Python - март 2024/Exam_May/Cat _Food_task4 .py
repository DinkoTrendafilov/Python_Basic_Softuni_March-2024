number_of_cats = int(input())

small_cats = 0
big_cats = 0
huge_cats = 0
food_price_per_kg = 12.45
total_food_in_grams = 0

for cat in range(1, number_of_cats + 1):
    cat_food_in_grams = float(input())
    total_food_in_grams += cat_food_in_grams

    if 100 <= cat_food_in_grams < 200:
        small_cats += 1
    elif 200 <= cat_food_in_grams < 300:
        big_cats += 1
    elif 300 <= cat_food_in_grams < 400:
        huge_cats += 1

total_price = (total_food_in_grams / 1000) * food_price_per_kg

print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {huge_cats} cats.")
print(f"Price for food per day: {total_price:.2f} lv.")


