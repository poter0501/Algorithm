import sys

n = sys.stdin.readline()
n = int(n)
if n == 1:
    print()
    exit()

i = 2
while n != 1:
    if n % i == 0:
        print(i)
        n = n // i
    else:
        i += 1
