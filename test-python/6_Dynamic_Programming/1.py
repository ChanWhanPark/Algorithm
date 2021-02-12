## 피보나치 수열
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2) ## 점화식

print(fibo(4))