## 1655. 가운데를 말해요 (10.12)
import heapq

n = int(input())
heap = []
for _ in range(n):
    i = int(input())
    heapq.heappush(heap, i)
    mid = len(heap) // 2
    if len(heap) % 2 == 0:
        print(heap[mid-1])
    else:
        print(heap[mid])