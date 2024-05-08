def solution(want, number, discount):
    answer = 0
    for i in range(0, len(discount)-9):
        sub_discount=discount[i:i+10]
        result=True
        for i, w in enumerate(want):
            if number[i]!=sub_discount.count(w):
                result=False
                break
        if result:
            answer+=1
            
    return answer