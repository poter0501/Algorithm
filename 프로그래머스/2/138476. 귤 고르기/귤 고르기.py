def solution(k, tangerine):
    answer = 0
    count={}
    for t in tangerine:
        if t in count:
            count[t]+=1
        else:
            count[t]=1
    
    for size, count in sorted(count.items(), reverse=True, key=lambda x:x[1]):
        k-=count
        answer+=1
        if k<=0:
            break

    return answer