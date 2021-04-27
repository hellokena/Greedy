import sys
n = int(sys.stdin.readline().rstrip())
level = []
cnt = 0
for _ in range(n):
    level.append(int(sys.stdin.readline().rstrip()))
    
# algorithm
for i in range(n-1, 0, -1): # 맨마지막에 얻는 골드값이 제일 커야 하므로 reverse
    if level[i-1] >= level[i]:
        # cnt : level[i]-1이 되기 위해 -1을 해야하는 횟수
        cnt += level[i-1] - (level[i] - 1)
        level[i-1] = level[i] - 1 # 최솟값을 구하는 것이므로 다음 인덱스 값 보다 1 작게
print(cnt)
