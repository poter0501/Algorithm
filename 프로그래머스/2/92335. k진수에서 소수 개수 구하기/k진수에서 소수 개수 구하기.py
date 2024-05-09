def solution(n, k):
    answer = 0
    k_string=get_k_string(n,k)
    targets=list(map(int, filter(lambda x: len(x)>0, k_string.split('0'))))
    
    for num in targets:
        if is_prime(num):
            answer+=1
    return answer

def get_k_string(n,k):
    result = ''
    while True:
        a, b = n//k, n%k
        result=str(b)+result
        if a<k:
            result=str(a)+result
            break
        n=a
    return result

def is_prime(num):
    if num==1:
        return False
    if num==2 or num==3:
        return True
    if num%2==0 or num%3==0:
        return False
    i=5
    while i*i<=num:
        if num%i==0 or num%(i+2)==0:
            return False
        i+=6
    return True
    
        
        