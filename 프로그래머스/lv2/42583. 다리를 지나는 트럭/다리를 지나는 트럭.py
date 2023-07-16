from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    que = deque(truck_weights)
    trucks_in_bridge = deque()
    weight_in_bridge = deque()
    while que:
        if trucks_in_bridge:
            tr, time = trucks_in_bridge[0]
            if time <= answer:
                trucks_in_bridge.popleft()
                weight_in_bridge.popleft()
                
        if len(weight_in_bridge) <= bridge_length:
            if sum(weight_in_bridge) + que[0] <= weight:
                truck = que.popleft()
                trucks_in_bridge.append((truck, answer + bridge_length))
                weight_in_bridge.append(truck)
            
        answer += 1
    # print(trucks_in_bridge)
    if trucks_in_bridge:
        answer = trucks_in_bridge[-1][1]+1
    return answer