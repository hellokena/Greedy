n = int(input())
array = list(map(int, input().split()))
array.sort()
s_sum = 0
result = 0
for i in array:
    s_sum += i
    result += s_sum
print(result)
