my_list = [10, 54, 61, 40, 21, 23, -7, -24, -97, -18, -11, 37, -67, 39]

print(f"Length of list is: {len(my_list)}")
print(f"Sum of list is: {sum(my_list)}")
print(f"Average value of list is: {sum(my_list) / len(my_list)}")

reversed_list = my_list[::-1]
sorted_list = sorted(my_list)
sorted_reversed_list = sorted(my_list)[::-1]

print(*my_list, sep=" ")
# print(*reversed_list, sep=", ")
print(*sorted_list, sep=", ")
# print(*sorted_reversed_list, sep=", ")
