## 괄호 변환 (10.09)
def divide(p):
    open = 0
    close = 0
    for i in range(len(p)):
        if p[i] == "(":
            open += 1
        else:
            close += 1
        if open == close:
            return p[:i+1], p[i+1:]

def balance(u):
    stack = []

    for uu in u:
        if uu == "(":
            stack.append(uu)
        elif uu == ")":
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    answer = ""
    # 과정 1
    if len(p) == 0:
        return ""
    # 과정 2
    u, v = divide(p)
    # 과정 3
    if balance(u):
        return u + solution(v)
    else:
        answer += "("
        answer += solution(v)
        answer += ")"
        for w in range(1, len(u)-1):
            if u[w] == "(":
                answer += ")"
            else:
                answer += "("
        return answer


p1 = "(()())()"
print(solution(p1))

p2 = ")("
print(solution(p2))

p3 = "()))((()"
print(solution(p3))