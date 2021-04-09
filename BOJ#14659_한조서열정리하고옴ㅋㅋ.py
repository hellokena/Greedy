dragon_num = int(input())
dragon = list(map(int, input().split()))
max = 0
for i in range(dragon_num): # 공격하는 드래곤
    temp = 0
    for j in range(i+1, dragon_num): # 공격받는 드래곤
        if dragon[i] < dragon[j]: break # 자기보다 큰 드래곤을 만나면 드러누움 / 다음 드래곤 보기
        else: temp += 1
    if max < temp: max = temp
print(max)
# 또한 용들은 처음 출발한 봉우리보다 높은 봉우리를 만나면
# 그대로 공격을 포기하고 금강산자락에 드러누워 낮잠을 청한다고 한다.
