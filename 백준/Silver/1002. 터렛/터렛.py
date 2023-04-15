import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif x1 == x2 and y1 == y2 and r1 != r2:
        print(0)
    else:
        dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if dist > max(r1, r2):
            if dist < (float)(r1 + r2):
                print(2)
            elif dist == (float)(r1 + r2):
                print(1)
            else:
                print(0)
        elif dist < max(r1, r2):
            if dist + min(r1, r2) < max(r1, r2):
                print(0)
            elif dist + min(r1, r2) > max(r1, r2):
                print(2)
            else:
                print(1)
        else:
            print(2)
