import sys
from itertools import combinations

while True:
    inputs = sys.stdin.readline().split()
    if inputs[0] == '0':
        break

    nums = inputs[1:]
    for com in combinations(nums, 6):
        print(' '.join(com))
    print()
