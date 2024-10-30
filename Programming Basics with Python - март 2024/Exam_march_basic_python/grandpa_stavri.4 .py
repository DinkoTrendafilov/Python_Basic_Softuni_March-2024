days = int(input())

total_liters = 0
total_liters_with_degrees = 0
average_degrees = 0

for day in range(1, days + 1):
    quantity_of_brandy = float(input())
    degrees_of_brandy = float(input())

    total_liters += quantity_of_brandy
    total_liters_with_degrees += quantity_of_brandy * degrees_of_brandy

average_degrees = total_liters_with_degrees / total_liters

print(f"Liter: {total_liters:.2f}")
print(f"Degrees: {average_degrees:.2f}")
if average_degrees < 38:
    print("Not good, you should baking!")
elif average_degrees > 42:
    print("Dilution with distilled water!")
else:
    print("Super!")
