import sys
from itertools import combinations

n, c = map(int, sys.stdin.readline().split())
x = []
max_pos = float('-inf')
min_pos = float('inf')

for _ in range(n):
    x.append(int(sys.stdin.readline()))
x.sort()

start = 1
end = x[-1] - x[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    count = 1
    last_position = x[0]
    
    for pos in x[1:]:
        if pos - last_position >= mid:
            count += 1
            last_position = pos
    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
