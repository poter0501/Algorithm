n, x = map(int, input().split())
data = map(int, input().split())
result = []
for d in data:
    if d < x:
        result.append(str(d))
print(' '.join(result))
