#1-4. 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence # 뮤터블 시퀀스

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2):
        a[i], a[n-i-1] = a[n-i-1], a[i]

if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬')
    n = int(input("원소 수 입력: "))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]값 입력: '))

    reverse_array(x)

    print('배열 원소를 역순으로 정렬')
    for i in range(n):
        print(f'x[{i}] = {x[i]}')