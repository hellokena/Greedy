sugar = int(input())
bag = 0

while True:
    if sugar%5 == 0:
        bag += (sugar//5)
        print(bag)
        break
    else:
        sugar -= 3
        bag += 1

    if sugar < 0:
        print(-1)
        break

# 우선 5의 배수인지 확인을 한다
# 5의 배수이면 바로 답을 도출하고
# 5의 배수가 아니면 3을 한번 빼본다,,,
# 그리고 다시 continue