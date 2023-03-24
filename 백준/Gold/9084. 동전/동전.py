import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())
    result = [0 for i in range(target + 1)]
    result[0] = 1
    
    for coin in coins:
        for money in range(coin, target + 1):
            result[money] += result[money - coin]

    print(result[target])