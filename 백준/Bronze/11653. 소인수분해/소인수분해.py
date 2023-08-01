import sys

n = sys.stdin.readline()
n = int(n)
if n == 1:
    print()
    exit()
is_prime = [True for i in range(n + 1)]
is_prime[0] = False
is_prime[1] = False

for i in range(2, n):
    if is_prime[i]:
        for j in range(1, n // i + 1):
            if j != 1:
                is_prime[i * j] = False

while not is_prime[n]:
    for i in range(2, n + 1):
        if n % i == 0:
            print(i)
            n = n // i
            break
print(n)
