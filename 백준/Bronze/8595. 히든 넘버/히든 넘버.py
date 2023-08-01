import sys

n = int(sys.stdin.readline())
word = sys.stdin.readline().rstrip()

hidden_num = ''
sum = 0
# ord('0') -> 48
# ord('9') -> 57
for c in word:
    if 48 <= ord(c) <= 57:
        hidden_num += c
    else:
        if hidden_num != '':
            sum += int(hidden_num)
            hidden_num = ''
            
if hidden_num!='':
    sum += int(hidden_num)
    hidden_num = ''
print(sum)
