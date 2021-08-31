## 부품 찾기 (08.31)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
sale_list = list(map(int, input().split()))
sale_list.sort() # 이진 탐색을 위한 정렬
m = int(input())
buy_list = list(map(int, input().split()))

for i in buy_list:
    result = binary_search(sale_list, i, 0, n-1)
    if result != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")