## 11866. 요세푸스 문제 0 (10.07)
n, m = map(int, input().split())
num_list = [i for i in range(1, n+1)]

print("<", end = "")
count = 0
while len(num_list) > 1:
    num = num_list.pop(0)
    count += 1
    if count == m:
        print("%d, " % num, end = "")
        count = 0
    else:
        num_list.append(num)

print("%d>" % num_list[0], end="")