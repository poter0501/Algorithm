import heapq

def solution(operations):
    answer = []    
    heap_min = []
    heap_max = []
    for opt in operations:
        if opt[0] == 'I':
            heapq.heappush(heap_min, int(opt[1:]))
            heapq.heappush(heap_max, -int(opt[1:]))
        else:
            if len(heap_min) != 0:
                if int(opt[1:]) < 0:
                    min_val = heapq.heappop(heap_min)
                    min_idx = heap_max.index(-min_val)
                    del heap_max[min_idx]
                    if len(heap_max) != 0:
                        heapq.heapify(heap_max)
                else:
                    max_val = heapq.heappop(heap_max)
                    max_idx = heap_min.index(-max_val)
                    del heap_min[max_idx]
                    if len(heap_min) != 0:
                        heapq.heapify(heap_min)
    
    if len(heap_max) == 0:
        answer.append(0)
        answer.append(0)
    else:
        answer.append(-heapq.heappop(heap_max))
        answer.append(heapq.heappop(heap_min))
        
    return answer