from itertools import combinations
import math

def solution(clothes):
    answer = 0
    clothe_dict = {}
    for clothe, ty in clothes:
        if ty in clothe_dict:
            clothe_dict[ty].append(clothe)
        else:
            clothe_dict[ty] = [clothe]
    types = list(clothe_dict.keys())
    
    if len(types) == len(clothes):
        for i in range(1, len(types)+1):
            answer+=math.comb(len(types), i)
        return answer
    
    combis = []
    
    for i in range(1, len(types)+1):
        for c in combinations(types, i):
            count = 1
            for ty in c:
                if ty in clothe_dict:
                    count *= len(clothe_dict[ty])
            answer += count
            count = 1
        
    return answer