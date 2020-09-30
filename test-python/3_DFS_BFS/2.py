def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i;
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

num = int(input("숫자를 입력하세요: "))
print('반복 구현: ', factorial_iterative(num))
print('재귀 구현: ', factorial_recursive(num))