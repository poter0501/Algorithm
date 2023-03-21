import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
add_count, sub_count, mul_count, div_count = map(int, sys.stdin.readline().split())
max_val = float('-inf')
min_val = float('inf')


def dfs(add, sub, mul, div, sum, idx):
    global max_val, min_val
    
    if idx == n:
        max_val = max(max_val, sum)
        min_val = min(min_val, sum)
        return
    else:
        if add > 0:
            dfs(add - 1, sub, mul, div, sum + numbers[idx], idx + 1)
        if sub > 0:
            dfs(add, sub - 1, mul, div, sum - numbers[idx], idx + 1)
        if mul > 0:
            dfs(add, sub, mul - 1, div, sum * numbers[idx], idx + 1)
        if div > 0:
            dfs(add, sub, mul, div - 1,
                sum // numbers[idx] if sum > 0 and numbers[idx] > 0 else -(abs(sum) // abs(numbers[idx])), idx + 1)


dfs(add_count, sub_count, mul_count, div_count, numbers[0], 1)
print(max_val)
print(min_val)