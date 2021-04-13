
import heapq

heap = [] # 힙 선언은 리스트 선언과 동일하다.

heapq.heappush(heap, 1) # 원소를 추가한다
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
heapq.heappush(heap, 4)
print(heap)

heapq.heappop(heap) # 가장 작은 값이 삭제된다
heapq.heappop(heap)
print(heap)

print(heap[0]) # 원소가 삭제되지 않으면서 가장 작은 값은 가져올 수 있다

array = [1, 2, 3, 4, 5]
heapq.heapify(heap) # 기존의 리스트를 힙으로 바꾼다
print(array)
