## 9012. 괄호 (10.04)
T = int(input())
answer = []
for test_case in range(1, T + 1):
    string = input()
    stack = []
    error_flag = 0
    for s in string:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if len(stack) == 0:
                error_flag = 1
                break
            else:
                stack.pop(-1)

    if len(stack) == 0 and error_flag == 0:
        print("YES")
    else:
        print("NO")



