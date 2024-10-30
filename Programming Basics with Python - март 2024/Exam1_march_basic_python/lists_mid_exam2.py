input_line = input().split(", ")
my_list = []

for num in input_line:
    my_list.append(num)

while True:
    command = input().split(" - ")
    if command[0] == "Craft!":
        break
    elif command[0] == "Collect":
        item = command[1]
        if item not in my_list:
            my_list.append(item)
    elif command[0] == "Drop":
        item = command[1]
        if item in my_list:
            my_list.remove(item)
    elif command[0] == "Combine Items":
        items = command[1].split(":")
        old_item = items[0]
        new_item = items[1]
        if old_item in my_list:
            index_old_item = my_list.index(old_item)
            my_list.insert(index_old_item + 1, new_item)
    elif command[0] == "Renew":
        item = command[1]
        if item in my_list:
            my_list.remove(item)
            my_list.append(item)

print(*my_list, sep=", ")
