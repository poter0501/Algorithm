import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
edges = {}
visited = [0 for i in range(n)]
parent = [-1 for i in range(n)]
for _ in range(n - 1):
    x, y = map(int, sys.stdin.readline().split())
    try:
        edges[x - 1].add(y - 1)
    except KeyError:
        edges[x - 1] = set()
        edges[x - 1].add(y - 1)
    try:
        edges[y - 1].add(x - 1)
    except KeyError:
        edges[y - 1] = set()
        edges[y - 1].add(x - 1)
        


def dfs(curr, pre):
    if visited[curr] != 0:
        return
    else:
        parent[curr] = pre
        visited[curr] = 1
        can_go = edges.get(curr, False)
        if can_go:
            for go in can_go:
                dfs(go, curr)
        return


dfs(0, 0)
for i in range(1, n):
    print(parent[i]+1)
