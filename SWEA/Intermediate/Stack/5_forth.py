## 4874. Forth(09.09)
T = int(input())
answer = []
for test_case in range(1, T + 1):
    stack = []
    forth = list(input().split())
    for i in range(len(forth)):
        if forth[i] == "+" or forth[i] == "-" or forth[i] == "*" or forth[i] == "/":
            if not stack or len(stack) == 1:
                answer.append("error")
                break
            else:
                a, b = stack.pop(-1), stack.pop(-1)
                if forth[i] == "+":
                    stack.append(b+a)
                elif forth[i] == "-":
                    stack.append(b-a)
                elif forth[i] == "*":
                    stack.append(b*a)
                elif forth[i] == "/":
                    stack.append(b//a)
        elif forth[i] == ".":
            if not stack or len(stack) >= 2:
                answer.append("error")
                break
            else:
                answer.append(stack.pop(-1))
        else:
            stack.append(int(forth[i]))


for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))