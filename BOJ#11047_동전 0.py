type_num, total = map(int, input().split())
coin_type = []
coin_num = 0
for i in range(type_num):
    coin_type.append(int(input()))
coin_type.sort(reverse=True)
for coin in coin_type:
    coin_num += total // coin
    total %= coin
print(coin_num)
