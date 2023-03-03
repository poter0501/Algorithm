n = int(input())
for i in range(n):
    data = list(map(int, input().split()))
    average_grade = sum(data[1:]) / data[0]
    high = list(filter(lambda x: x > average_grade, data[1:]))
    print('{:.3f}%'.format(100*len(high)/data[0]))
