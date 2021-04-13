import sys
import heapq

def solution(n,heap):
    result = 0
    for i in range(n-1):
        temp1 = heapq.heappop(heap)
        temp2 = heapq.heappop(heap)
        result += temp1 + temp2
        heapq.heappush(heap, temp1 + temp2)
    print(result)

heap = []
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    heapq.heappush(heap,(int(sys.stdin.readline().rstrip())))

solution(n,heap)
