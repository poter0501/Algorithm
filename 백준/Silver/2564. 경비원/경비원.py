import sys
from collections import deque

l, h = map(int, sys.stdin.readline().split())
shop_count = int(sys.stdin.readline().rstrip())
shop = deque()

for _ in range(shop_count + 1):
    direction, distance = map(int, sys.stdin.readline().split())
    x = distance if direction == 1 or direction == 2 else 0 if direction == 3 else l
    y = (h - distance) if direction == 3 or direction == 4 else 0 if direction == 2 else h
    shop.append([x, y, direction])

x_start, y_start, direction_start = shop.pop()
dist_min = 0
face_directions = [0, 2, 1, 4, 3]
while shop:
    x_shop, y_shop, direction_shop = shop.popleft()
    if direction_shop == direction_start:  # in the same line
        dist_min += abs(x_start - x_shop) + abs(y_start - y_shop)
        continue
    
    if face_directions[direction_start] != direction_shop:  # in the enclosed line
        dist_min += abs(x_start - x_shop) + abs(y_start - y_shop)
        continue
    # in the faced line
    if direction_start == 1 or direction_start == 2:
        path1 = (l - x_start) + (l - x_shop) + h
        path2 = x_start + x_shop + h
        dist_min += min(path1, path2)
    else:
        path1 = (h - y_start) + (h - y_shop) + l
        path2 = y_start + y_shop + l
        dist_min += min(path1, path2)

print(dist_min)
