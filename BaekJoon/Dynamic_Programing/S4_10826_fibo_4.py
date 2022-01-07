## 10826. 피보나치 수 4 (01.07) S4

n = int(input())

fibo = [0, 1, 1]
for i in range(3, n+1):
    fibo.append(fibo[i-1]+fibo[i-2])

print(fibo[n])