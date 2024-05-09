from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for sequence in permutations(dungeons, len(dungeons)):
        answer=max(count(k, sequence), answer)
        
    return answer

def count(k, dungeons):
    count=0
    for start_k, consume_k in dungeons:
        if k>=start_k:
            count+=1
            k-=consume_k
        else:
            break
    return count