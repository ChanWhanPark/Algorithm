## 14501. 퇴사 (10.08)
n = int(input())
t = []
p = []
com_list = [0] * (n+1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        com_list[i] = max(p[i] + com_list[time], max_value)
        max_value = com_list[i]
    else:
        com_list[i] = max_value

print(max_value)
