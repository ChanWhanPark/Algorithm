## 4866. 괄호검사(09.08)

def check(str):
    s = []
    for i in str:
        if i == "{" or i == "(":
            s.append(i)
        elif i == "}" or i == ")":
            if s:
                a = s.pop()
            else:
                return 0
            if a == "{" and i == ")":
                return 0
            if a == "(" and i == "}":
                return 0
    if s:
        return 0
    else:
        return 1

T = int(input())
answer = []
for test_case in range(1, T + 1):
    sentence = input()
    answer.append(check(sentence))

print(answer)
for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))