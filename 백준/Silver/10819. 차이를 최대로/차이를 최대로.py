import sys


def recursive_func(input_list, num):
    result = []
    if num == 1:
        result = [[i] for i in input_list]
        return result
    else:
        for i in range(len(input_list)):
            if i == 0:
                result = result + [j + [input_list[i]] for j in recursive_func(input_list[i + 1:], num - 1)]
            elif i == len(input_list) - 1:
                result = result + [j + [input_list[i]] for j in recursive_func(input_list[:i], num - 1)]
            else:
                result = result + [j + [input_list[i]] for j in
                                   recursive_func(input_list[:i] + input_list[i + 1:], num - 1)]
    return result


def operating(input_list):
    result = 0
    for i in range(len(input_list) - 1):
        result = result + abs(input_list[i] - input_list[i + 1])
    return result


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
permutations = recursive_func(a, n)
operated_vals = [operating(p) for p in permutations]
print(max(operated_vals))
