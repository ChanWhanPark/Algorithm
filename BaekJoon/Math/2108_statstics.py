## 2108. 통계학 (01.03)
n = int(input())
array = []
sum = 0
for _ in range(n):
    array.append(int(input()))

array.sort()
# 1. 산술평균
for i in range(n):
    sum += array[i]
print(sum//n)
# 2. 중앙값
print(array[n//2])
# 3. 최빈값
temp = 0
max_value = 0
temp_array = []
for i in range(n):
    for j in range(i+1, n):
        if array[i] == array[j]:
            temp += 1
    if temp > max_value:
        max_value = temp
        temp_array = []
        temp_array.append(array[i])
    elif temp == max_value:
        temp_array.append(array[i])
temp_array.sort()
if len(temp_array) < 2:
    print(temp_array[0])
else:
    print(temp_array[1])

# 4. 범위
print(array[-1]-array[0])
