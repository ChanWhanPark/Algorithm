array = [9, 6, 1, 4, 3, 7, 8, 2, 0, 5]

for i in range(len(array)):
    min_index = i # 최솟값 설정
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # Swap


print(array)