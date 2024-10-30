number_of_people = int(input())
season = input()

price_per_person = 0

if number_of_people <= 5:
    if season == "spring":
        price_per_person = 50
    elif season == "summer":
        price_per_person = 48.5
    elif season == "autumn":
        price_per_person = 60
    elif season == "winter":
        price_per_person = 86

elif number_of_people > 5:
    if season == "spring":
        price_per_person = 48
    elif season == "summer":
        price_per_person = 45
    elif season == "autumn":
        price_per_person = 49.5
    elif season == "winter":
        price_per_person = 85

total_price = number_of_people * price_per_person

if season == "summer":
    total_price *= 0.85
elif season == "winter":
    total_price *= 1.08

print(f"{total_price:.2f} leva.")
