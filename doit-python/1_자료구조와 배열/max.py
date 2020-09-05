# 1-1. 시퀀스 원소의 최댓값 출력

from typing import Any, Sequence

def max_of(a: Sequence)-> Any:
    max = a[0]
    for i in range(len(a)):
        if a[i] >= max:
            max = a[i]
    return max

if __name__ == '__main__':
    print("배열 최댓값 구하기")
    n = int(input("원소 수 입력: "))
    x = [None] * n # 리스트 생성
    for i in range(n):
        x[i] = int(input(f'x[{i}]값 : '))

    print(f'최댓값 = {max_of(x)}')
