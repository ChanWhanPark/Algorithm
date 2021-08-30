## 삽입 정렬 (08.30)
array = list(map(int, input().split()))

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]: # 앞 인덱스가 더 큰 경우 계속해서 교체
            array[j], array[j-1] = array[j-1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)