n = int(input())
for i in range(n):
    result = []
    ox = input()
    temp = []
    for idx, c in enumerate(ox):
        if c == 'O':
            temp.append(c)
        if idx == len(ox) - 1 or c == 'X':
            if len(temp) != 0:
                result.append(len(temp))
            temp = []
    answer = 0
    for re in result:
        answer = answer + ((re + 1) * re) / 2
    print(int(answer))

