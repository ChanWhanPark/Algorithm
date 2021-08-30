## 위에서 아래로(08.30)
# T 기업 코딩테스트

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array.sort(reverse=True)

for i in array:
    print(i, end=' ')