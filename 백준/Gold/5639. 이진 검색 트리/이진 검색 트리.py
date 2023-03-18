import sys

sys.setrecursionlimit(10 ** 6)
numbers = []
while True:
    try:
        num = int(sys.stdin.readline())
        numbers.append(num)
    except:
        break


def postorder(start, end):
    if start > end:
        return
    mid = end + 1
    
    for i in range(start + 1, end + 1):
        if numbers[start] < numbers[i]:
            mid = i
            break
    
    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(numbers[start])


postorder(0, len(numbers) - 1)
