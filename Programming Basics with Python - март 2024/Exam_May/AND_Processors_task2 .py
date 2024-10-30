import math

needed_processors = int(input())
worker_count = int(input())
working_days_count = int(input())

total_working_time = working_days_count * worker_count * 8
making_processors = math.floor(total_working_time / 3)

processor_price = 110.10
count_of_processors = abs(needed_processors - making_processors)

if needed_processors > making_processors:
    loses = count_of_processors * processor_price
    print(f"Losses: -> {loses:.2f} BGN")

else:
    profit = count_of_processors * processor_price
    print(f"Profit: -> {profit:.2f} BGN")

