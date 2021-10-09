## 가장 큰 수 (10.09)
'''
from itertools import permutations
def solution(numbers):
    answer = ''
    max_value = 0
    per = permutations(numbers, len(numbers))
    for p in per:
        temp = ''
        for i in range(len(numbers)):
            temp += str(p[i])
        if int(temp) > max_value:
            max_value = int(temp)
            answer = temp

    return answer
'''

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x : x*3, reverse=True)

    return str(int(''.join(numbers)))


print(solution([6, 10, 2]))