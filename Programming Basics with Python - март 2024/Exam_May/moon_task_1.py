import math

average_speed = float(input())
fuel_in_liters_per_100_km = float(input())

total_distance = 384_400 * 2
time_to_go = math.ceil(total_distance / average_speed)
total_time = time_to_go + 3
needed_fuel = int((fuel_in_liters_per_100_km * total_distance) / 100)


print(total_time)
print(needed_fuel)

