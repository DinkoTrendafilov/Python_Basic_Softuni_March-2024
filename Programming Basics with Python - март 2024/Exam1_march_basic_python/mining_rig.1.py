import math

price_of_video_card = int(input())
price_of_transition = int(input())
price_of_electricity_from_card_per_day = float(input())
profit_from_card_per_day = float(input())

total_price_of_cards = price_of_video_card * 13
total_price_of_transitions = price_of_transition * 13
total_spend_money = total_price_of_cards + total_price_of_transitions + 1000

profit_of_card = profit_from_card_per_day - price_of_electricity_from_card_per_day
total_profit_of_cards = 13 * profit_of_card

days_of_return = math.ceil(total_spend_money / total_profit_of_cards)

print(total_spend_money)
print(days_of_return)
