## 1629. 곱셈 (10.08)
def multiply(a, b, c):
    if b == 1:
        return a % c
    else:
        temp = multiply(a, b//2, c)
        if b % 2 == 0:
            return temp**2 % c
        else:
            return a * (temp**2) % c

a, b, c = map(int, input().split())
print(multiply(a, b, c))