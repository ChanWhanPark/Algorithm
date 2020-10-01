n, m = list(map(int, input().split(' '))) # 떡의 개수 n, 떡의 길이 m

array = list(map(int, input().split())) # 떡의 개별 높이 정보

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += (x - mid)
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)