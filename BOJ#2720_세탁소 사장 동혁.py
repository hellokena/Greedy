coin = [25, 10, 5, 1]
t = int(input())
for i in range(t):
    exchange = [0, 0, 0, 0]
    money = int(input())
    for i in range(4):
        exchange[i] = money//coin[i]
        money = money%coin[i]
    print(' '.join(map(str, exchange)))
