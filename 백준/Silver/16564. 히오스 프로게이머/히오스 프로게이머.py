import sys

n, k = map(int, sys.stdin.readline().split())

xi = []
for _ in range(n):
    xi.append(int(sys.stdin.readline()))
team_obj_level = 0

low = min(xi)
upper = max(xi)
while k > 0:
    if low == upper:
        low = k // n + low
        break
    mid = (low + upper) // 2
    if mid == low:
        k -= (upper - low) * xi.count(low)
        if k >= 0:
            xi = [upper] * n
            low = upper
    else:
        gaps = list(filter(lambda x: x < mid, xi))
        gaps_sum = mid * len(gaps) - sum(gaps)
        if len(gaps) == 0:
            break
        if gaps_sum <= k:
            k -= gaps_sum
            low = mid
            xi = list(filter(lambda x: x >= mid, xi)) + [mid] * len(gaps)
        else:
            upper = mid
print(low)
