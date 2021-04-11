import sys
test_case = int(sys.stdin.readline())
for i in range(test_case):
    n = int(sys.stdin.readline())
    candidate = []
    count = 1 # resume 순으로 오름차순 정렬을 할때 맨처음 정렬되는 건 반드시 선발됨
    for j in range(n):
        resume, interview = list(map(int, sys.stdin.readline().split()))
        candidate.append([resume, interview])
    candidate.sort(key=lambda x:x[0])
    min_interview = candidate[0][1]
    # 앞사람보다 인터뷰 점수가 높으면
    for k in range(1,n):
        if candidate[k][1] < min_interview: # 면접점수가 이전보다 작으면(등수가 높으면)
            min_interview = candidate[k][1]
            count += 1
    print(count)
