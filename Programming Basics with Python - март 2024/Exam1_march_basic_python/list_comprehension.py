nums = [num for num in range(1, 16)]  # list comprehension
nums1 = [num for num in range(1, 16) if num % 2 == 1]  # list comprehension + if
nums2 = [num if num % 2 == 0 else num + 100 for num in range(1, 16)]  # if - else

print(*nums, sep=" ")
print(*nums1, sep=" ")
print(*nums2, sep=" ")
