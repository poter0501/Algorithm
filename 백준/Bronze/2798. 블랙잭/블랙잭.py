import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

answer = float('-inf')
for pmt in permutations(cards, 3):
    sum_val = sum(pmt)
    if answer < sum_val <= m:
        answer = sum_val
        if sum_val == m:
            break
print(answer)
