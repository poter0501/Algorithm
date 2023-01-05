def solution(nums):
    answer = 0
    
    N=len(nums)/2
    s=set(nums)
    s_len = len(s)
    if s_len>=N:
        answer=N
    else:
        answer=s_len
    
    return answer