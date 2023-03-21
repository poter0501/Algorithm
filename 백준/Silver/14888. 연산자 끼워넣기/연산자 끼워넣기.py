import copy
import sys
from itertools import permutations

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
operator_dict = {0: '+', 1: '-', 2: '*', 3: '/'}
operators = []
for i, operator_count in enumerate(list(map(int, sys.stdin.readline().split()))):
    for j in range(operator_count):
        operators.append(operator_dict[i])
# print(operators)
val_min = float('inf')
val_max = float('-inf')
for way in map(list, permutations(operators, len(operators))):
    temp_a = copy.deepcopy(a)
    left_side = temp_a.pop(0)
    right_side = temp_a.pop(0)
    while True:
        oprt = way.pop(0)
        if oprt == '+':
            left_side = left_side + right_side
        elif oprt == '-':
            left_side = left_side - right_side
        elif oprt == '*':
            left_side = left_side * right_side
        else:
            if left_side < 0:  # right_side 의 경우 a 리스트 안에 있던 원소라 항상 양수
                left_side = abs(left_side) // abs(right_side)
                left_side = -left_side
            else:
                left_side = left_side // right_side
        if len(temp_a) > 0:
            right_side = temp_a.pop(0)
        else:
            break
    if left_side < val_min:
        val_min = left_side
    if left_side > val_max:
        val_max = left_side
print(val_max)
print(val_min)