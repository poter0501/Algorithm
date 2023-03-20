# 위상 정렬
# 진입차수가 0인 노드를 큐에 넣는다.
# 진입 차수(indegree) -> 나한테 오는 간선 수
# 진출 차수(outdegree) -> 내가 갈 수 있는 간선 수
# 큐가 빌 때까지 다음의 과정을 반복한다.
# 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
# 새롭게 진입차수가 0이 된 노드를 큐에 삽입

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

degree = [0 for i in range(n)]
order = {i: set() for i in range(n)}
for _ in range(m):
    small, tall = map(int, sys.stdin.readline().split())
    small -= 1
    tall -= 1
    degree[tall] += 1
    order[small].add(tall)

que = deque()
already_visited = [False for i in range(n)]
for i, dgr in enumerate(degree):
    if dgr == 0 and not already_visited[i]:
        que.append(i)
result = []
loop = True
while que:
    target = que.popleft()
    for i in order[target]:  # delete
        degree[i] = max(degree[i] - 1, 0)
        if degree[i] == 0:
            que.append(i)
    
    if not already_visited[target]:
        already_visited[target] = True
        result.append(target + 1)

print(' '.join(map(str, result)))
