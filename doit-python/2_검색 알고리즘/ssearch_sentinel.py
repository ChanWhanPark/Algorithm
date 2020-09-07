# 2-3. 보초법 사용 선형 알고리즘

from typing import Any, Sequence
import copy

def seq_search(a: Sequence, k: Any) -> int:
    seq = copy.deepcopy(a) # seq에 x를 복사
    seq.append(k) # 보초 k를 추가

    i = 0
    while True:
        if a[i] == key:
            break # 검색 성공 시 while 문 종료
        i += 1

    return -1 if i == len(seq) else i
    # 보초로 검색 시 -1 반환 아닐시 위치 반환

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