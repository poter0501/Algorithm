def solution(s):
    answer = ''
    start = 0
    
    for i in range(len(s)):
        if s[i] != ' ':
            if i == start:
                answer += s[i].upper()
            else:
                answer += s[i].lower()
        else:
            answer += s[i]
            start = i+1
        # print(answer)
    return answer