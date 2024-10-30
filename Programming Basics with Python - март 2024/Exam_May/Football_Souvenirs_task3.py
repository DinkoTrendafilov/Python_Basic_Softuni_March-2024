team_name = input()
type_item = input()
count_of_items = int(input())

single_price = 0
is_wrong_country = False
is_wrong_stock = False


if team_name == "Argentina":
    if type_item == "flags":
        single_price = 3.25
    elif type_item == "caps":
        single_price = 7.20
    elif type_item == "posters":
        single_price = 5.10
    elif type_item == "stickers":
        single_price = 1.25
    else:
        is_wrong_stock = True

elif team_name == "Brazil":
    if type_item == "flags":
        single_price = 4.2
    elif type_item == "caps":
        single_price = 8.50
    elif type_item == "posters":
        single_price = 5.35
    elif type_item == "stickers":
        single_price = 1.20
    else:
        is_wrong_stock = True

elif team_name == "Croatia":
    if type_item == "flags":
        single_price = 2.75
    elif type_item == "caps":
        single_price = 6.90
    elif type_item == "posters":
        single_price = 4.95
    elif type_item == "stickers":
        single_price = 1.10
    else:
        is_wrong_stock = True


elif team_name == "Denmark":
    if type_item == "flags":
        single_price = 3.10
    elif type_item == "caps":
        single_price = 6.50
    elif type_item == "posters":
        single_price = 4.80
    elif type_item == "stickers":
        single_price = 0.90
    else:
        is_wrong_stock = True

else:
    is_wrong_country = True

total_price = single_price * count_of_items

if total_price > 0:
    print(f"Pepi bought {count_of_items} {type_item} of {team_name} for {total_price:.2f} lv.")

else:
    if is_wrong_country:
        print("Invalid country!")
    else:
        print("Invalid stock!")
