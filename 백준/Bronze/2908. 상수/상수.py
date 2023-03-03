x, y = map(str, input().split())
print(int(x[2] + x[1] + x[0])) if int(x[2] + x[1] + x[0])>int(y[2] + y[1] + y[0]) else print(int(y[2] + y[1] + y[0]))
