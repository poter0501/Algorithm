import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
bin_codes = []
for _ in range(n):
    bin_codes.append(sys.stdin.readline().rstrip())
a, b = map(int, sys.stdin.readline().split())
a -= 1
b -= 1

can_go = [[] for i in range(n)]
# 해밍 경로의 길이가 1인 경로 찾기
for i in range(n):
    for j in range(i + 1, n):
        s = bin_codes[i]
        e = bin_codes[j]
        count = 0
        for idx in range(k):
            if count > 1:
                break
            if s[idx] != e[idx]:
                count += 1
        if count == 1:
            can_go[i].append(j)
            can_go[j].append(i)

que = deque([[a]])
visited = [[0 for i in range(n)] for j in range(n)]
visited[a][a] = 1
while que:
    path = que.popleft()
    start = path[-1]
    for go in can_go[start]:
        if visited[start][go] == 0:
            que.append(path + [go])
            visited[start][go] = 1
            visited[go][start] = 1
            if go == b:
                print(' '.join(map(str, [e + 1 for e in path + [go]])))
                exit()
print(-1)
