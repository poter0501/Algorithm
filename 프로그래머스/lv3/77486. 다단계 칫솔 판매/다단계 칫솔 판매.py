def solution(enroll, referral, seller, amount):
    answer = []
    
    temp={}
    temp={n[0]:[n[1], 0] for n in zip(enroll, referral)}
    
    for i in zip(seller, amount):
        s=i[0]
        total=i[1]*100
        
        while s!='-':
            pay=total//10
            net=total-pay
            temp[s][1]+=net
            if pay<=0:
                break
            s=temp[s][0]
            total=pay
    
    answer=list(map(lambda x: temp[x][1] , enroll))
    return answer