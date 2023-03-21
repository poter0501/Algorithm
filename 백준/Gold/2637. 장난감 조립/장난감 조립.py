import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

is_base = [i for i in range(n + 1)]
graph = [[] for i in range(n + 1)]
in_degree = [0 for i in range(n + 1)]
for _ in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    is_base[x] = 0
    in_degree[x] += k
    graph[y].append([x, k])

base = set(filter(lambda p: p != 0, is_base))
# print(f'base={base}')
# print(f'in_degree={in_degree}')
# print(f'graph={graph}')

part_count = [[0 for i in range(n + 1)] for j in range(n + 1)]

que = deque(base)
while que:
    part = que.popleft()
    if part in base:  # base part
        for i in range(len(graph[part])):
            mid_part = graph[part][i][0]
            count = graph[part][i][1]
            
            part_count[mid_part][part] += count
            graph[part][i][1] = 0
            in_degree[mid_part] -= count
        in_degree[part] = -1
    else:  # mid part
        for i in range(len(graph[part])):
            mid_part = graph[part][i][0]
            count = graph[part][i][1]
            if count != 0:
                temp = [t * count for t in part_count[part]]
                part_count[mid_part] = [temp[i] + part_count[mid_part][i] for i in range(n + 1)]
                graph[part][i][1] = 0
                in_degree[mid_part] -= count
        in_degree[part] = -1
    # find zero degree
    for z in range(1, n + 1):
        if in_degree[z] == 0:
            que.append(z)

for re in sorted(list(base)):
    print(f'{re} {part_count[n][re]}')