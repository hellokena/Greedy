time_array = [300, 60, 10]
count_array= [0, 0, 0]
remain_time = int(input())
for i in range(3):
    count_array[i] += remain_time // time_array[i]
    remain_time %= time_array[i]
if remain_time != 0: print(-1)
else: print(' '.join(map(str, count_array)))
