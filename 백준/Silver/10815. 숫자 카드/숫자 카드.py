import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
cards.sort()


def bisect_search(num):
    start = 0
    end = n - 1
    mid = (start + end) // 2
    if cards[start] == num or cards[mid] == num or cards[end] == num:
        return 1
    while start < mid < end:
        if num < cards[mid]:
            end = mid
        elif num > cards[mid]:
            start = mid
        else:
            return 1
        
        mid = (start + end) // 2
        if cards[start] == num or cards[mid] == num or cards[end] == num:
            return 1
    return 0


answer = [str(bisect_search(num)) for num in nums]
print(' '.join(answer))
