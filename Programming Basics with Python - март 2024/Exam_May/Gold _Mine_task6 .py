number_of_locations = int(input())

for location in range(1, number_of_locations + 1):
    expected_average_yield = float(input())
    days_of_work = int(input())

    daily_yield = 0
    real_average_yield = 0

    for day in range(1, days_of_work + 1):
        day_yield = int(input())
        daily_yield += day_yield

    real_average_yield = daily_yield / days_of_work

    if real_average_yield >= expected_average_yield:
        print(f"Good job! Average gold per day: {real_average_yield:.2f}.")
    else:
        diff = abs(real_average_yield - expected_average_yield)
        print(f"You need {diff:.2f} gold.")
