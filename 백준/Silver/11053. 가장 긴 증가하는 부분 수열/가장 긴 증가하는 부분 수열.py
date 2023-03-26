import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

result = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if sequence[j] < sequence[i]:
            result[i] = max(result[i], result[j] + 1)
            
print(max(result))