import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    # print(scoville)
    
    while scoville and len(scoville) >= 2:
        if scoville[0]>=K:
            break
        answer += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second*2)
    
    if len(scoville) < 2 and scoville[0] < K:
        return -1
    
    return answer