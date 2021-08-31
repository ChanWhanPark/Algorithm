## 순차 탐색 (08.31)

def sequential_search(n, target, array):
    for i in range(n):
        if target == array[i]:
            return i+1

## 생성할 원소 갯수와 찾을 문자열 입력
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

## 문자열 입력
array = input.split()

print(sequential_search(n, target, array))