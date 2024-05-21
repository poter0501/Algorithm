def solution(topping):
    answer = 0
    a={topping[0]:1}
    b={}
    for i in range(1, len(topping)):
        if topping[i] in b:
            b[topping[i]]+=1
        else:
            b[topping[i]]=1
    idx=1
    while idx<len(topping):
        if topping[idx] in a:
            a[topping[idx]]+=1
        else:
            a[topping[idx]]=1
            
        if topping[idx] in b:
            b[topping[idx]]-=1
            if b[topping[idx]]==0:
                b.pop(topping[idx])
        
        if len(a)==len(b):
            answer+=1
        idx+=1

    return answer