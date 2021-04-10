n = int(input())
timetable = []

for i in range(n):
    start, end = map(int, input().split())
    timetable.append([start, end])

timetable.sort(key=lambda x:(x[1], x[0]))

num = 1 # 회의실 갯수
end = timetable[0][1]

for i in range(1, n):
    if timetable[i][0] >= end:
        num += 1
        end = timetable[i][1]

print(num)
