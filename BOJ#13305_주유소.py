import sys
n = int(sys.stdin.readline().rstrip())
road = list(map(int, sys.stdin.readline().rstrip().split())) #n-1개
oil = list(map(int, sys.stdin.readline().rstrip().split())) #n개

result = road[0]*oil[0]
minprice = oil[0] # 맨 처음의 기름값을 최솟값으로 둔다

for i in range(1, n-1): # 마지막 인덱스는 no
    if oil[i] < minprice: # 기름값이 더 최솟값이 나오면
        result += road[i] * oil[i]
        minprice = oil[i] # 최솟값 갱신
    else: # 그게 아닐 경우 이전에 저장해두었던 최솟값으로 진행
        result += road[i] * minprice

print(result)
