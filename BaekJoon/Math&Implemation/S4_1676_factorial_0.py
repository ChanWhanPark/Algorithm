## 1676. 팩토리얼 0의 개수(01.08) S4
n = int(input())
fact = [1] * 501

def factorial(n):
    for i in range(1, n+1):
        fact[i] = fact[i-1] * i

factorial(n)
last_num = str(fact[n])
length = len(last_num)
index = length - 1
zero_count = 0

while True:
    if last_num[index] != '0':
        break
    else:
        zero_count += 1

    index -= 1

print(zero_count)