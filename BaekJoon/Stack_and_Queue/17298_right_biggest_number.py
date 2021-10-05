## 17298. 오큰수 (10.05)

'''
n = int(input())
nge = list(map(int, input().split()))
right_biggest = []
index = []
for i in range(n):
    for j in range(i+1, n):
        if nge[i] < nge[j]:
            right_biggest.append(nge[j])
            index.append(i)
            break
        if j == n-1:
            right_biggest.append(-1)

for r in right_biggest:
    print(r, end=' ')
'''

n = int(input())
nge = list(map(int, input().split()))

right_biggest = [-1] * n
stack = []

for i in range(n):
    while stack and stack[-1][0] < nge[i]:
        tmp, idx = stack.pop()
        right_biggest[idx] = nge[i]
    stack.append([nge[i], i])

for n in right_biggest:
    print(n, end=' ')