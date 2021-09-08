## 4865. 글자수 (09.08)
T = int(input())
answer = []
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    count_list = []

    for i in str1:
        count_list.append(str2.count(i))

    answer.append(max(count_list))




for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))