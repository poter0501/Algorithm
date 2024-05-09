from collections import deque

def solution(numbers, target):
    answer=0
    ways=deque([0])
    idx=0
    for i, num in enumerate(numbers):
        while ways and len(ways)<2**(i+1):
            midterm = ways.popleft()
            ways.append(midterm+num)
            ways.append(midterm-num)
    return ways.count(target)