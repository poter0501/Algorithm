import sys

n = int(sys.stdin.readline())

# map_input = [[int(c) for c in sys.stdin.readline().rstrip()] for i in range(n)]
map_input = []
total_zero_count = 0
for _ in range(n):
    line = [int(c) for c in sys.stdin.readline().rstrip()]
    total_zero_count += line.count(0)
    map_input.append(line)

# find start position of search
start = [0, 0]
loop = True
for i in range(n):
    if not loop:
        break
    for j in range(n):
        if map_input[i][j] == 1:
            start = [i, j]
            loop = False
            break

group_num = 2


def dfs(now_x, now_y, homes):
    if map_input[now_x][now_y] != 1:
        return
    else:
        map_input[now_x][now_y] = group_num
        num = now_x * n + now_y
        homes.add(num)
        move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for move_x, move_y in move:
            next_x = now_x + move_x
            next_y = now_y + move_y
            if 0 <= next_x < n and 0 <= next_y < n:
                dfs(next_x, next_y, homes)


home_groups_count = []
home_groups = set()
idx = 0
while sum(home_groups_count) + total_zero_count < n ** 2:
    if idx == 0:
        idx += 1
        home = set()
        dfs(start[0], start[1], home)
        home_groups_count.append(len(home))
        home_groups.union(home)
        group_num += 1
    else:
        for i in range(n):
            for j in range(n):
                if map_input[i][j] == 1 and (i * n + j) not in home_groups:  # 아직 방문 하지 않은곳
                    home = set()
                    dfs(i, j, home)
                    home_groups_count.append(len(home))
                    home_groups.union(home)
                    group_num += 1

print(len(home_groups_count))
for cnt in sorted(home_groups_count):
    print(cnt)