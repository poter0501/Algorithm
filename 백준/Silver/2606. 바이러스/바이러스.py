import sys

com_count = int(sys.stdin.readline())
pair_count = int(sys.stdin.readline())

parent = [i for i in range(com_count)]


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
        for i, n in enumerate(parent):
            if n == root_y:
                parent[i] = root_x
    elif root_x > root_y:
        for i, n in enumerate(parent):
            if n == root_x:
                parent[i] = root_y
    # if root_x != root_y:
    #     for i, n in enumerate(parent):
    #         if n == root_y:
    #             parent[i] = root_x


for _ in range(pair_count):
    a, b = map(int, sys.stdin.readline().split())
    if a < b:
        union(a - 1, b - 1)
    else:
        union(b - 1, a - 1)
ans = parent.count(0)-1
print(ans)
