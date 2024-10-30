n = int(input())
is_found = False
count = 0

for a in range(1, 10):
    for b in range(9, 0, -1):
        for c in range(0, 10):
            for d in range(9, -1, -1):
                multiple = a * b * c * d
                sum_of_a_b_c_d = a + b + c + d
                if multiple == sum_of_a_b_c_d and n % 10 == 5:
                    count = 1
                    print(f"{a}{b}{c}{d}")
                    is_found = True
                    break

                elif multiple // sum_of_a_b_c_d == 3 and n % 3 == 0:
                    count = 1
                    print(f"{d}{c}{b}{a}")
                    is_found = True
                    break
            if is_found:
                break
        if is_found:
            break
    if is_found:
        break

if count == 0:
    print("Nothing found")
