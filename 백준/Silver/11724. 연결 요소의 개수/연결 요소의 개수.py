import sys

n, m = map(int, sys.stdin.readline().split())

parent = [i for i in range(0, n)]


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x < root_y:
        # parent[y] = root_x
        for i, p in enumerate(parent):
            if p == root_y:
                parent[i] = root_x
    elif root_x > root_y:
        # parent[x] = root_y
        for i, p in enumerate(parent):
            if p == root_x:
                parent[i] = root_y


for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    union(x - 1, y - 1)

parent = set(parent)
print(len(parent))
