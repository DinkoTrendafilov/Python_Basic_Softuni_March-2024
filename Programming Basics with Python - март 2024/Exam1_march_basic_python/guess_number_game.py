target_number = int(input("Въведи число между 1 и 100 за познаване: "))

while not 1 <= target_number <= 100:
    print("Моля, въведете число между 1 и 100")
    target_number = int(input("Въведи число между 1 и 100 за познаване: "))
counter = 0

while True:

    your_number = int(input("Въведи твоето число: "))

    if your_number == target_number:
        print(f"Поздравления! Ти откри {target_number}.")
        break
    if your_number > target_number:
        print(f"Твоето число е по-голямо от числото за познаване: ")
    else:
        print(f"Твоето число е по-малко от числото за познаване: ")
    counter += 1
    if counter >= 5:
        print(f"Много съжаляваме!\nТи изгуби играта, ти направи {counter} грешни отговора")
        break
