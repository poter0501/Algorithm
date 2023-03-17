# 정답 찾아봄
# 스패닝 트리란
# 최소 간선의 수를 갖는 서브트리
# 최소 스패닝 트리란
# 스패닝 트리 중 가중치의 값의 합이 최소치인 경우

# Kruskal 알고리즘
# 간선 들의 가중치를 기준으로 오름차순으로 정렬하고
# 가장 작은 가중치를 갖는 간선들 부터 순차적으로 선택하고
# 선택된 간선이 이미 선택된 간선들과 사이클 or 루프를 생성 하는지 검사
# 사이클을 생성하면 pass -> 스패닝 트리에 맞지 않기 때문
# 사이클을 판별하는 알고리즘은 union-find 알고리즘

# union-find 알고리즘

import sys

v, e = map(int, sys.stdin.readline().split())

lines = []
for _ in range(e):
    lines.append(list(map(int, sys.stdin.readline().split())))

lines.sort(key=lambda x: x[2])  # 가중치 값 기준 오름차순 정렬
min_cost = 0
parent = [i for i in range(v)]


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    parent[root_y] = root_x
    return root_x


for i in range(e):
    start, end, weight = lines[i]
    if find(start - 1) != find(end - 1):  # 루프를 만들지 않는다
        if start < end:
            union(start - 1, end - 1)
        else:
            union(end - 1, start - 1)
        min_cost += weight
    else:  # 루프를 만든다
        pass

print(min_cost)
