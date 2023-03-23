import sys
import re

n = int(sys.stdin.readline())

result = [0 for i in range(n+1)]
if n <= 2:
    print(n)
    exit()
result[1] = 1
result[2] = 2
idx = 3
while idx <= n:
    result[idx] = (result[idx - 1] + result[idx - 2]) % 15746
    idx += 1

print(result[n])