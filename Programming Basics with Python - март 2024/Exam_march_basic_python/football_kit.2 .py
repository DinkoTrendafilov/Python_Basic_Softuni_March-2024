price_t_shirt = float(input())
needed_money = float(input())

price_shorts = price_t_shirt * 0.75
price_socks = price_shorts * 0.2
price_buttons = (price_t_shirt + price_shorts) * 2

sum_of_products = price_t_shirt + price_shorts + price_socks + price_buttons
discount = sum_of_products * 0.15

total_sum = sum_of_products - discount

if total_sum >= needed_money:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum:.2f} lv.")
else:
    diff = abs(needed_money - total_sum)
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")
