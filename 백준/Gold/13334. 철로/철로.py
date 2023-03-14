import sys
import heapq

n = int(sys.stdin.readline())

pairs = []
for _ in range(n):
    pairs.append(sorted(list(map(int, sys.stdin.readline().split()))))

d = int(sys.stdin.readline())
# n = 8
# pairs = [[25, 35], [10, 20], [10, 25], [30, 50], [50, 60], [25, 30], [80, 100]]
# d = 30

pairs.sort(key=lambda x: (x[1], x[0]))
# print(pairs)
count = 0
heap = []

for i in range(len(pairs)):
    start = pairs[i][0]
    end = pairs[i][1]
    
    if end - start <= d:
        heapq.heappush(heap, pairs[i][0])
    
    while len(heap) > 0:
        temp_start = heap[0]
        if end - temp_start <= d:
            break
        else:
            heapq.heappop(heap)
    count = max(count, len(heap))

print(count)
