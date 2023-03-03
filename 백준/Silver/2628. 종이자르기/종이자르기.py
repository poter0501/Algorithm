w, h = map(int, input().split())
n = int(input())

before_cutting = [[0, 0, w, h]]
after_cutting = []
result = []
for i in range(n):
    command, line = map(int, input().split())
    if command == 0:  # cut horizontal
        for square in before_cutting:
            if square[1] <= line <= square[3]:
                after_cutting.append([square[0], line, square[2], square[3]])
                after_cutting.append([square[0], square[1], square[2], line])
            else:
                after_cutting.append(square)

    else:  # cut vertical
        for square in before_cutting:
            if square[0] <= line <= square[2]:
                after_cutting.append([line, square[1], square[2], square[3]])
                after_cutting.append([square[0], square[1], line, square[3]])
            else:
                after_cutting.append(square)

    before_cutting = after_cutting
    after_cutting = []
    # print(before_cutting)
    result = [(a[2] - a[0]) * (a[3] - a[1]) for a in before_cutting]
print(max(result))
