import sys
import heapq

n = int(sys.stdin.readline())
max_heap = []
for _ in range(n):
    command = int(sys.stdin.readline())
    if command == 0:
        try:
            print(-heapq.heappop(max_heap))
        except IndexError:
            print(0)
    else:
        heapq.heappush(max_heap, -command)
