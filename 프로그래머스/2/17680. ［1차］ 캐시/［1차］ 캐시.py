from collections import deque

def solution(cacheSize, cities):
    answer = 0
    if cacheSize==0:
        return len(cities)*5
    cache = []
    cities = deque(cities)
    
    while cities:
        city = cities.popleft().lower()
        if city in cache:
            answer+=1
            cache.remove(city)
            cache.append(city)
            continue
        
        answer+=5
        if len(cache)<cacheSize:
            cache.append(city)
            continue
        if len(cache)>=cacheSize:
            del cache[0]
            cache.append(city)
            
    return answer