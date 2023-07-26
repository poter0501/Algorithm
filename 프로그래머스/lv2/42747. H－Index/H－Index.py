# [8, 7, 6, 5, 0] => 4
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    # citations = [6, 5, 4, 1, 0]
    print(citations)
    for i, ct in enumerate(citations):
        count = i+1
        print(f'count= {count}, citation= {ct}')
        if count >= ct:
            return ct
        
        if i<len(citations)-1 and count>citations[i+1]:
            return count
        
        if i==len(citations)-1 and count<ct:
            return count
            
    return answer