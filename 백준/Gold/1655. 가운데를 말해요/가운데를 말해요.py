import heapq
import sys

min_heap = []
max_heap = []
n = int(sys.stdin.readline())
initial_val = 0
for i in range(1, n + 1):
    val = int(sys.stdin.readline())
    if i == 1:
        print(val)
        initial_val = val
        # min_heap.append(val)
    elif i == 2:
        if val >= initial_val:
            max_heap.append(-initial_val)
            min_heap.append(val)
            print(initial_val)
        else:
            max_heap.append(-val)
            min_heap.append(initial_val)
            print(val)
    else:
        # mid1 = -max_heap[0]
        # mid2 = min_heap[0]
        
        if val >= -max_heap[0]:
            heapq.heappush(min_heap, val)
        else:
            heapq.heappush(max_heap, -val)
        
        if len(max_heap) > len(min_heap) + 1:
            temp = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, temp)
        elif len(max_heap) + 1 < len(min_heap):
            temp = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -temp)
        
        if len(max_heap) == len(min_heap):
            print(-max_heap[0])
        else:
            if len(max_heap) > len(min_heap):
                print(-max_heap[0])
            else:
                print(min_heap[0])
