## 1003. 피보나치 수열 (10.07 01.07) S3
# 1003의 C++ 함수에서 출력되는 0과 1의 개수를 구함

zero = [1, 0, 1] # ... 1, 2, 3
one = [0, 1, 1] # ... 2, 3, 5

def fibo(n):
    length = len(zero)
    if length <= n:
        for i in range(length, n + 1): # 계속해서 데이터 추가
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])

    print(zero[n], one[n])

t = int(input())
for _ in range(t):
    n = int(input())
    fibo(n)

