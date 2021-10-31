## 1026. 보물(10.30)
n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list = sorted(a_list)
b_list = sorted(b_list, reverse=True)

result = 0
for i in range(n):
    result += (a_list[i] * b_list[i])

print(result)