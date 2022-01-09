## 10773. 제로 (01.09) S4
n = int(input())
num_list = []

for _ in range(n):
    num = int(input())
    if num == 0:
        num_list.pop()
    else:
        num_list.append(num)

if len(num_list) == 0:
    print(0)
else:
    print(sum(num_list))