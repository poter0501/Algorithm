import sys

n = int(sys.stdin.readline())

result = [0, 1]
idx = 2
while idx <= n:
    result.append(result[idx - 1] + result[idx - 2])
    idx += 1
print(result[n])