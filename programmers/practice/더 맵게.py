## 더 맵게 (10.07)
import heapq

def solution(scovile, k):
    heap = []
    for s in scovile:
        heapq.heappush(heap, s)

    answer = 0
    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + 2 * heapq.heappop(heap))
        except:
            return -1
        answer += 1

    return answer

scovile = [1, 2, 3, 9, 10, 12]
k = 7

print(solution(scovile, k))