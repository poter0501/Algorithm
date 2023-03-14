import sys

# m = 4
# n = 8
# l = 4
# pos_fire = [6, 1, 4, 9]
# pos_fire.sort()
# pos_animal = [[7, 2], [3, 3], [4, 5], [5, 1], [2, 2], [1, 4], [8, 4], [9, 4]]


m, n, l = map(int, sys.stdin.readline().split())

pos_fire = [i for i in map(int, sys.stdin.readline().split())]
pos_fire.sort()
pos_animal = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if y <= l:
        pos_animal.append([x, y])


def distance(x, a):
    return abs(x - a[0]) + a[1]


# print(pos_fire)
# print(pos_animal)
count = 0
for fire in pos_fire:
    pos_animal.sort(key=lambda z: distance(fire, z))
    # print(pos_animal)
    start = 0
    end = len(pos_animal) - 1
    if distance(fire, pos_animal[start]) > l:
        break
    else:
        while start < end:
            mid = (start + end) // 2
            
            if distance(fire, pos_animal[mid]) <= l:
                count += (mid - start) + 1
                start = mid + 1
            else:
                end = mid
            if start == len(pos_animal) - 1:
                if distance(fire, pos_animal[start]) <= l:
                    count += 1
        pos_animal = pos_animal[start:]
print(count)
