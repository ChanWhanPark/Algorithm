## 1158. 요세푸스 문제 (01.09) S5
n, m = map(int, input().split())
num_list = [i for i in range(1, n+1)]

answer = []
num = 0

for t in range(n):
    num += m-1
    if num >= len(num_list):
        num = num % len(num_list)
    answer.append(str(num_list.pop(num)))

print("<", ", ".join(answer)[:], ">", sep="")

