## 두 배열의 원소 교체(08.30)
# 국제 알고리즘 대회

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    a[i], b[i] = b[i], a[i]


sum = 0
for i in range(len(a)):
    sum += a[i]

print(sum)