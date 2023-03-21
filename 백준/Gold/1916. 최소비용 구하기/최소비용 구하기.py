import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
edges = [[] for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    
    edges[a].append((c, b))

start, end = map(int, sys.stdin.readline().split())
min_cost = [float('inf') for i in range(n + 1)]
visited = [False for i in range(n + 1)]


def func(st):
    heap = []
    heapq.heappush(heap, (0, st))
    min_cost[st] = 0
    visited[st] = True
    while heap:
        w, pos = heapq.heappop(heap)
        
        if min_cost[pos] < w:
            continue
        
        for nxt_w, nxt_node in edges[pos]:
            if nxt_w + min_cost[pos] < min_cost[nxt_node]:
                min_cost[nxt_node] = nxt_w + min_cost[pos]
                heapq.heappush(heap, (min_cost[nxt_node], nxt_node))


func(start)
print(min_cost[end])