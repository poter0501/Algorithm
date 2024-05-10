def solution(msg):
    answer = []
    idx_dict = {chr(i): i-64 for i in range(65, 91)}
    curr=0
    max_idx=26
    
    while curr<len(msg):
        if curr==len(msg)-1:
            answer.append(idx_dict[msg[curr]])
            return answer
            
        nxt=curr+1
        while True:
            sub_str=msg[curr: nxt+1]
            
            if sub_str in idx_dict:
                if nxt==len(msg)-1:
                    answer.append(idx_dict[sub_str])
                    return answer
                nxt+=1
            else:
                max_idx+=1
                idx_dict[sub_str]=max_idx
                answer.append(idx_dict[msg[curr:nxt]])
                break
        curr=nxt
    return answer