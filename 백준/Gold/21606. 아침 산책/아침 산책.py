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


def dfs(curr, count=0):
    if visited[curr] != 0:
        return
    else:
        if in_out[curr] == 1 and count != 0:
            path.append(curr)
            return
        else:
            visited[curr] = 1
            path.append(curr)
            can_go = edges.get(curr, False)
            if can_go:
                for go in can_go:
                    dfs(go, count + 1)


# print(f' 실내외: {in_out}')
total_count = 0
for i, in_or_out in enumerate(in_out):
    if in_or_out == 1:
        dfs(i)
        # print(f'start={i}, path = {path}')
        start_idx = 0
        end_idx = start_idx + 1
        possible = []
        for p in path[1:]:
            if in_out[p] == 1:
                possible.append(p)
                total_count += 1
        # print(f'start={i}, possible={possible}')
        path = list()
        visited = [0 for i in range(n)]
print(total_count)
