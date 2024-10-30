cat_breed = input()
cat_gender = input()

cat_years = 0

if cat_gender == "m":
    if cat_breed == "British Shorthair":
        cat_years = 13
    elif cat_breed == "Siamese":
        cat_years = 15
    elif cat_breed == "Persian":
        cat_years = 14
    elif cat_breed == "Ragdoll":
        cat_years = 16
    elif cat_breed == "American Shorthair":
        cat_years = 12
    elif cat_breed == "Siberian":
        cat_years = 11


elif cat_gender == "f":
    if cat_breed == "British Shorthair":
        cat_years = 14
    elif cat_breed == "Siamese":
        cat_years = 16
    elif cat_breed == "Persian":
        cat_years = 15
    elif cat_breed == "Ragdoll":
        cat_years = 17
    elif cat_breed == "American Shorthair":
        cat_years = 13
    elif cat_breed == "Siberian":
        cat_years = 12

cat_months = round(cat_years * 12 / 6)

if cat_years == 0:
    print(f"{cat_breed} is invalid cat!")
else:
    print(f"{cat_months} cat months")
