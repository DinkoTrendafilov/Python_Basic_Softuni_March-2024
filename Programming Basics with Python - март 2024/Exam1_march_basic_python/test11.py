my_list = [int(number) for number in input().split()]

avg = sum(my_list) / len(my_list)
my_other_list = [1, 33, -9, -5, 23, 145, 111, -73, -97, 88, 14, 19, -22, -11, 27, -34, -100, -19, 29, -23, -45, 97, 21,
                 -89, 2, 3, 4, 13, 17]

print(*sorted(my_list), sep=" ")
print(len(my_list))
print(sum(my_list))
print(avg)
print(*my_other_list)
