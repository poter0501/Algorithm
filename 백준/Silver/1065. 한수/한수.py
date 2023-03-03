n = int(input())
count = 99
if n <= 99:
    print(n)
else:
    for i in range(100, n + 1):
        if i != 1000:
            digits = [int(digit) for digit in str(i)]
            gap1 = digits[0] - digits[1]
            gap2 = digits[1] - digits[2]
            if gap1 == gap2:
                count = count + 1
    print(count)
