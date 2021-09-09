## 4873. 반복되는 문자 지우기(09.09)

T = int(input())
answer = []
for test_case in range(1, T + 1):
    sentence = list(input())
    stack = []
    for i in range(len(sentence)):
        if not stack or stack[-1] != sentence[i]:
            stack.append(sentence[i])
        elif stack and stack[-1] == sentence[i]:
            stack.pop()

    answer.append(len(stack))

for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))