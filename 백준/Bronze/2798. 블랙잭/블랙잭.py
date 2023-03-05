import sys


def combination(combi, num):
    result = []
    if num == 1:
        result = [[i] for i in combi]
        return result
    else:
        for i, c in enumerate(combi):
            if i == 0:
                result = result + [[combi[i]] + j for j in combination(combi[i + 1:], num - 1)]
            elif i == len(combi) - 1:
                result = result + [[combi[i]] + j for j in combination(combi[:i], num - 1)]
            else:
                result = result + [[combi[i]] + j for j in combination(combi[:i] + combi[i + 1:], num - 1)]
    return result


n, m = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))
combinations = combination(cards, 3)
sum_list = [sum(i) for i in combinations]
sum_list = list(filter(lambda x: x <= m, sum_list))
print(max(sum_list))
