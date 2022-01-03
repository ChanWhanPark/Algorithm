## 2805. 나무 자르기 (01.03)

n, cut = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end: # 시작값과 끝값이 교차하는 부분
    mid = (start + end) // 2

    log = 0
    for i in tree:
        if i > mid:
            log += i - mid

    # 총 벌목값을 잘라야할 양과 비교
    if log >= cut: # 자른 게 많으면 시작값 증가
        start = mid + 1
    else: # 적으면 끝값 감소
        end = mid - 1

print(end)
