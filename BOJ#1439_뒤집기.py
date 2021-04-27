import sys
num = list(sys.stdin.readline().rstrip())
sep = []
temp = [num[0]]
for i in range(1, len(num)):
    if num[i-1] == num[i]: # 같은 수라면
        temp.append(num[i])
    else:
        sep.append(temp)
        temp = [num[i]] # 초기화
sep.append(temp)
zero = 0
one = 0
for i in sep:
    if i[0] == '0': zero += 1
    else: one += 1

print(min(one, zero))
