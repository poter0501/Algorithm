import sys

k, n = map(int, sys.stdin.readline().split())
lengths = []

for _ in range(k):
    lengths.append(int(sys.stdin.readline().rstrip()))


def total_count(num):
    count = 0
    for l in lengths:
        count += l // num
    return count


upper = max(lengths)
lower = 1
answer = 0
while lower <= upper:
    mid = (upper + lower) // 2
    cnt = total_count(mid)
    
    if cnt < n:
        upper = mid - 1
    else:
        lower = mid + 1
        answer = mid
print(answer)