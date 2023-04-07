# 풀이 시작 11:00am
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
gift_box = [[-i, i] for i in map(int, sys.stdin.readline().split())]
children_demand = list(map(int, sys.stdin.readline().split()))

result = 1
heapq.heapify(gift_box)
# print(gift_box)
for c in children_demand:
    try:
        dummy, g_max = heapq.heappop(gift_box)
        if g_max < c:
            result = 0
            break
        else:
            if g_max - c > 0:
                heapq.heappush(gift_box, [-(g_max-c), (g_max-c)])
    except:
        result = 0
        break

print(result)