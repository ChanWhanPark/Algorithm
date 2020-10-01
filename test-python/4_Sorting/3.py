array = [9, 6, 1, 4, 3, 7, 8, 2, 0, 5]

def quick_sort(array):
    if len(array) < 1:
        return array

    pivot = array[0] # 피벗은 첫 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))