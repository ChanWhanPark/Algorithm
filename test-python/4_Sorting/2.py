array = [9, 6, 1, 4, 3, 7, 8, 2, 0, 5]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # i부터 0까지 -1씩 감소
        if array[j] < array[j-1]: # 한칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j] # Swap
        else:
            break

print(array)