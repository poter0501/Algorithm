import sys
import heapq

n = int(sys.stdin.readline())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(sys.stdin.readline()))

result = 0
while len(cards) > 1:
    a1 = heapq.heappop(cards)
    a2 = heapq.heappop(cards)
    result += a1 + a2
    heapq.heappush(cards, a1 + a2)

print(result)
