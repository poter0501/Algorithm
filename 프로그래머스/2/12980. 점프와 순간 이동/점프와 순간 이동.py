def solution(n):
    return bin(n).count('1')
#     result = {}
    
#     for i in range(1, n+1):
#         if i==1:
#             result[i]=1
#         elif i%2==0:
#             result[i] = min(result[i-1]+1, result[i//2])
#         else:
#             result[i]= result[i-1]+1
    
#     return result[n]
