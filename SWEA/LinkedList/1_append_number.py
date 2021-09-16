## 5108. 숫자 추가 (09.16)

T = int(input())
answer = []
for test_case in range(1, T + 1):
    n, m, l = map(int, input().split())
    data = list(map(int, input().split()))
    for _ in range(m):
        data.insert(*map(int, input().split()))


    answer.append(data[l])





for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))