a = int(input())
b = input()

for digit in range(len(b) - 1, -1, -1):
    print(a*int(b[digit]))
print(a*int(b))
