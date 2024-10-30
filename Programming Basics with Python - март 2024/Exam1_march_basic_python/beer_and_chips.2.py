import math

football_fan_name = input()
budget = float(input())
number_of_bottles_beer = int(input())
number_of_chips = int(input())

price_of_beer = 1.2
price_of_chips = 0.45 * number_of_bottles_beer * price_of_beer

sum_of_chips = math.ceil(price_of_chips * number_of_chips)
sum_of_beer = price_of_beer * number_of_bottles_beer

total_price = sum_of_chips + sum_of_beer

diff = abs(budget - total_price)

if budget >= total_price:
    print(f"{football_fan_name} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{football_fan_name} needs {diff:.2f} more leva!")
