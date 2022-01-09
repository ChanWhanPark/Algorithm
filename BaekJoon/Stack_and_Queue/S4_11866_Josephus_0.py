## 11866. 요세푸스 문제 0 (10.07, 01.09) S4
n, k = map(int, input().split())
num_list = [i for i in range(1, n+1)]

answer = []
count = 0
while len(num_list) > 0:
    num = num_list.pop(0)
    count += 1
    if count == k:
        answer.append(str(num))
        count = 0
    else:
        num_list.append(num)


print("<", ", ".join(answer), ">", sep="")