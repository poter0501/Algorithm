def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for ele in arr:
        if len(answer) == 0:
            answer.append(ele)
            continue
            
        if ele != answer[-1]:
            answer.append(ele)
            
    return answer