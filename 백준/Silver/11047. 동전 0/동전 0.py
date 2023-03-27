import sys

n, k = map(int, sys.stdin.readline().split())

coins = []
for _ in range(n):
    c = int(sys.stdin.readline())
    if c <= k:
        coins.append(c)

sum_money = k
coin_count = 0
while sum_money > 0:
    coin = coins.pop()
    coin_count += sum_money // coin
    sum_money = sum_money % coin
print(coin_count)