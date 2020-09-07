#2-4. 이진 검색 알고리즘

from typing import Any, Sequence

def bin_search(a: Sequence, k: Any) -> int:
    pl = 0 # 맨 앞 원소의 인덱스
    pr = len(a) - 1 # 맨 뒤 원소의 인덱스

    while True:
        pc = (pl + pr) // 2 # 중앙 원소의 인덱스
        if a[pc] == key:
            return pc # 검색 성공
        elif a[pc] < key:
            pl = pc + 1 # 검색 범위를 뒤로 좁힘
        else:
            pr = pc - 1 # 검색 범위를 앞으로 좁힘
        if pl > pr:
            break

    return -1


if __name__ == '__main__':
    num = int(input("원소 수 입력: "))
    x = [None] * num  # 원소 수 num인 리스트 생성

    print('배열 데이터를 오름차순으로 입력\n\n')
    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i-1]: # 오름차순이 아닐 시 종료
                break

    key = int(input('검색할 값 입력: '))

    idx = bin_search(x, key)

    if idx == -1:
        print('검색값이 없습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')