n = int(input())
numbers = list(map(int, input().split()))
count = 0
for number in numbers:
    if number == 2:
        count = count + 1
    else:
        for i in range(2, number):
            if number % i == 0:
                break
            if i == number - 1:
                count = count + 1
print(count)
