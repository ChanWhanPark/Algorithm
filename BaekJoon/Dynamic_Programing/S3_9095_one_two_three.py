## 9095. 1,2,3 더하기 (10.08 01.07) S3
def plus(n):
    if n == 1:
        return 1 # 1
    elif n == 2:
        return 2 # 1+1, 2
    elif n == 3:
        return 4 # 1+1+1, 1+2, 2+1, 3
    else:
        return plus(n-1) + plus(n-2) + plus(n-3)


t = int(input())
for _ in range(t):
    n = int(input())
    print(plus(n))