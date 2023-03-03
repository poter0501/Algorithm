for i in range(int(input())):
    n, text = list(map(str, input().split()))
    n = int(n)
    result = ''
    for c in text:
        result = result + c * n
    print(result)
