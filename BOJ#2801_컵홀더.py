# 컵홀더를 사용할 수 있는 사람
n = int(input())
seat = input()
cnt = seat.count('LL')
if cnt <= 1: print(n)
else: print(n-(cnt-1))
