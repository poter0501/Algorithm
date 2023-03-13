import copy
import sys

n, b = map(int, sys.stdin.readline().split())

input_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def mul_matrix(a_matrix, b_matrix, c):
    result_matrix = [[0] * n] * n
    for i in range(n):
        result_matrix_row = []
        row = a_matrix[i]
        for j in range(n):
            col = [b_matrix[k][j] for k in range(n)]
            temp = [(row[l] * col[l]) % c for l in range(n)]
            result_matrix_row.append(sum(temp) % c)
        result_matrix[i] = result_matrix_row
    
    return result_matrix


result_dict = {}


def f(matrix, x):
    try:
        return copy.deepcopy(result_dict[x])
    except KeyError:
        pass
    
    if x == 1:
        temp = copy.deepcopy(matrix)
        for i in range(n):
            for j in range(n):
                temp[i][j] = temp[i][j] % 1000
        result_dict[x] = temp
        return copy.deepcopy(result_dict[x])
    else:
        result_dict[x] = mul_matrix(f(copy.deepcopy(matrix), x // 2), f(copy.deepcopy(matrix), x - (x // 2)), 1000)
        return copy.deepcopy(result_dict[x])


for r in f(input_matrix, b):
    print(' '.join(map(str, r)))
