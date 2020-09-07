#2-2. 선형 검색 알고리즘 / for문 사용
from typing import Any, Sequence

def seq_search(a: Sequence, k: Any) -> int:
    i = 0

    for i in range(len(a)):
       if a[i] == key:
           return i
    return -1


if __name__ == '__main__':
    num = int(input("원소 수 입력: "))
    x = [None] * num # 원소 수 num인 리스트 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    key = int(input('검색할 값 입력: '))

    idx = seq_search(x, key)

    if idx == -1:
        print('검색값이 없습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')