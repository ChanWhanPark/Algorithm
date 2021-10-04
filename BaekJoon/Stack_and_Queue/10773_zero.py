## 10773. 제로 (10.04)
k = int(input())
answer = []
for _ in range(k):
    num = int(input())
    if num == 0:
        answer.pop(-1)
    else:
        answer.append(num)

if len(answer) == 0:
    print(0)
else:
    print(sum(answer))