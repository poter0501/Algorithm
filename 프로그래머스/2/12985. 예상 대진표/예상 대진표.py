def solution(n,a,b):
    answer = 0
    r=1
    a-=1
    b-=1
    while True:
        if a//2==b//2:
            return r
        else:
            a=a//2
            b=b//2
        r+=1
    

    return answer