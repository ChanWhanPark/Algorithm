#1-3. 배열 원소의 최댓값 구해 출력

import random
from max import max_of # max.py의 max_of 함수 사용

print('난수의 최댓값')
num = int(input('난수의 개수: '))
small = int(input('난수의 최솟값: '))
big = int(input('난수의 최댓값: '))
x = [None] * num

for i in range(num):
    x[i] = random.randint(small, big)

print(f'{(x)}')
print(f'최댓값 : {max_of(x)}')