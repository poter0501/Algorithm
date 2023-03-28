import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    grade = [0 for _ in range(n)]
    for i in range(n):
        doc_grade, intrv_grade = map(int, sys.stdin.readline().split())
        grade[n - doc_grade] = intrv_grade
    
    # print(grade)
    count = 1
    temp = grade.pop()
    while grade:
        if grade[-1] > temp:
            grade.pop()
        else:
            temp = grade.pop()
            count += 1
    
    print(count)
