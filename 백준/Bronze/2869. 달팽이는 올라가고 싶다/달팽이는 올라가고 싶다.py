a, b, v = map(int, input().split())
# ad-bd>=v -> d >=v/(a-b)
# ad-b(d-1)>=v -> ad-bd+b >=v -> d(a-b)+b >=v -> d>=(v-b)/(a-b)

temp1 = int(v / (a - b)) + 1 if v / (a - b) - int(v / (a - b)) > 0 else int(v / (a - b))
temp2 = int((v - b) / (a - b)) + 1 if (v - b) / (a - b) - int((v - b) / (a - b)) > 0 else int((v - b) / (a - b))
print(min(temp1, temp2))
