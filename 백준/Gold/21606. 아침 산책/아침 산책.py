import sys

sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline())
in_out = [int(c) for c in sys.stdin.readline().rstrip()]
edges = {}
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

visited = [0 for i in range(n)]
path = []

i = []
ii = []


def dfs(curr, pre):
    if visited[curr] != 0:
        return
    else:
        visited[curr] = 1
        if in_out[curr] == 0:  # outside
            can_go = edges.get(curr, False)
            if can_go:
                for go in can_go:
                    dfs(go, curr)
        elif in_out[curr] == 1:  # inside
            if in_out[pre] == 1:
                ii.append([pre, curr])
            else:
                i.append(curr)
            can_go = edges.get(curr, False)
            if can_go:
                for go in can_go:
                    dfs(go, curr)


# print(edges)
# print(f'실내외: {in_out}')
try:
    out_idx = in_out.index(0)
    dfs(out_idx, out_idx)
    print(len(i)*2+len(ii)*2)
except ValueError:
    pass