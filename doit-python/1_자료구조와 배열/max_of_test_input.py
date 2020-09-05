# 1-2. 배열의 최댓값 구해 출력

from max import max_of # max.py의 max_of 함수 사용

print('배열의 최댓값 구하기')
print('주의: "End"를 입력하면 종료')

num = 0
x = []

while True:
    s = input(f'x[{num}]값 입력: ')
    if s == 'End':
        break
    x.append(int(s))
    num += 1

print(f'{num}개 입력')
print(f'최댓값 {max_of(x)}')