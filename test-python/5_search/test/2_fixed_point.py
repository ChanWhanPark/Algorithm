## 고정점 찾기

def binary_search(data, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if data[mid] == mid:
        return mid
    elif data[mid] < mid:
        return binary_search(data, mid+1, end)
    else:
        return binary_search(data, start, mid-1)


n = int(input())
data = list(map(int, input().split()))
data.sort()

result = binary_search(data, 0, n-1)
if result == None:
    print(-1)
else:
    print(result)