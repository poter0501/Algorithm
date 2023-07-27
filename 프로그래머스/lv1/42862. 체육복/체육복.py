def solution(n, lost, reserve):
    # 본인의 체육복을 잃어버렸지만 여분을 가지고 있는 학생들을 처리
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

    for r in set_reserve:
        if r - 1 in set_lost:
            set_lost.remove(r - 1)
        elif r + 1 in set_lost:
            set_lost.remove(r + 1)

    # 전체 학생 수에서 체육복을 못 빌린 학생들을 제외
    answer = n - len(set_lost)

    return answer
