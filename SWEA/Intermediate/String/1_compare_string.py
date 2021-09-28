## 4864. 문자열 비교(09.07)
T = int(input())
answer = []
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    if str1 in str2:
        answer.append(1)
    else:
        answer.append(0)

for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))