def solution(n, t, m, p):
    answer = ''
    idx=[ i*m+p-1 for i in range(t)]
    all_str=''
    num=0
    while True:
        all_str+=n_num_str(n,num)
        num+=1
        if len(all_str)>idx[-1]:
            break
    for i in idx:
        answer+=all_str[i]
    
    return answer

def n_num_str(n, num):
    if n==10 or num==0:
        return str(num)
    
    result = ''
    al = ['A', "B", "C", "D", "E", "F"]
    while num > 0:
        digit = num % n
        if digit<10:
            result = str(digit) + result
        else:
            result = al[digit - 10] + result
        num //= n
    
    return result