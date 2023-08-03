import sys
from itertools import permutations

n = int(sys.stdin.readline())
nums = [str(i) for i in range(1, n+1)]
for pmt in permutations(nums, n):
    print(' '.join(pmt))
