## 1912. 연속 합 (01.08) S2
n = int(input())
num_list = list(map(int, input().split()))
sum = [num_list[0]]

for i in range(len(num_list)-1):
    sum.append(max(num_list[i+1], num_list[i+1] + sum[i]))

print(max(sum))