percent_fats = int(input())
percent_proteins = int(input())
percent_carbohydrates = int(input())
total_calories = int(input())
percent_water = int(input())

one_gram_fats = 9
one_gram_proteins = 4
one_gram_carbohydrates = 4

total_fats = ((percent_fats * total_calories) / 100) / 9
total_proteins = ((percent_proteins * total_calories) / 100) / 4
total_carbohydrates = ((percent_carbohydrates * total_calories) / 100) / 4

total_food = total_fats + total_carbohydrates + total_proteins
calories_per_gram_food = total_calories / total_food

water_in_calories = (percent_water * calories_per_gram_food) / 100

calories = calories_per_gram_food - water_in_calories

print(f"{calories:.4f}")
