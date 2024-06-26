import heapq

def solution(people, limit):
    answer = 0
    people.sort()
    left=0
    right=len(people)-1
    while left<=right:
        if left==right:
            answer+=1
            break
        if people[left]+people[right]<=limit:
            answer+=1
            right-=1
            left+=1
            continue
        if people[left]+people[right]>limit:
            answer+=1
            right-=1
        
    return answer
        
    
    