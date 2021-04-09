dragon_num = int(input())
dragon = list(map(int, input().split()))

maximum = 0 # 공격하는 드래곤
cnt = 0 # 처지할 드래곤의 수
temp = 0 # 더 큰 봉우리를 만났을 때, 그 이전까지의 갯수

for d in dragon: 
    if d > maximum: # 해당 드래곤이 지금까지의 가장 높았던 드래곤보다 높을 때
        maximum = d # 가장 높은 드래곤 갱신
        cnt = 0 # 처치할 드래곤 새로 새우기 위해서 0 초기화
    else:
        cnt += 1 # 계속해서 가장 높았던 드래곤보다 낮으면 처치할 드래곤수 ++
    temp = max(temp, cnt) # 지금까지의 처치한 드래곤 수가 많나 이전에 처리한 드래곤 수가 많나 비교
print(temp)
