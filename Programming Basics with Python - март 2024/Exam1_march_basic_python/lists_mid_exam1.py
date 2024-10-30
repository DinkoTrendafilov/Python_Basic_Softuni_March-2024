my_list = [int(num) for num in input().split()]

while True:
    command = input().split()
    if command[0] == "end":
        break

    elif command[0] == "swap":
        index1 = int(command[1])
        index2 = int(command[2])
        my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

    elif command[0] == "multiply":
        index1 = int(command[1])
        index2 = int(command[2])
        my_list[index1] *= my_list[index2]

    elif command[0] == "decrease":
        my_list = [num - 1 for num in my_list]

print(*my_list, sep=", ")
