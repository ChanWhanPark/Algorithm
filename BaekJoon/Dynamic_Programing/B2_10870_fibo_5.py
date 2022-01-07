## 10870. 피보나치 수 5 (01.07) B2
def fibo(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)

n = int(input())
print(fibo(n))