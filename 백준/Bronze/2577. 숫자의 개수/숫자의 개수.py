a = int(input())
b = int(input())
c = int(input())
result = str(a * b * c)
count = [0] * 10
for digit in result:
    count[int(digit)] = count[int(digit)] + 1

for result in count:
    print(result)
