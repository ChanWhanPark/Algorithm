## 괄호 변환(08.31)
# 2020 카카오 신입 공채 1차

def balanced_index(p):
    left_count = 0
    for i in range(len(p)):
        if p[i] == "(":
            left_count += 1
        else:
            left_count -= 1
        if left_count == 0:
            return i

def check_proper(p):
    left_count = 0
    for i in p:
        if i == '(':
            left_count += 1
        else:
            if left_count == 0: # 쌍이 맞지 않을 경우 False
                return False
            left_count -= 1
    return True # 쌍이 맞을 경우 True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p) # 괄호가 전체적으로 맞는 부분의 인덱스 확인
    # 그 인덱스를 기준으로 나눔
    u = p[:index+1]
    v = p[index+1:]
    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫번째 문자와 마지막 문자 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += "".join(u)
    return answer

p = input()
print(solution(p))