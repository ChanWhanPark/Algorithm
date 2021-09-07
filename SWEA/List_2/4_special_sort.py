## 4843. 특별한 정렬 (09.07)

T = int(input())
answer = []
for test_case in range(1, T + 1):
    n = int(input())
    data = list(map(int, input().split()))
    result = []
    data.sort()
    for i in range(5):
        result.append(data[-(i+1)])
        result.append(data[i])
    answer.append(result)

for test_case in range(T):
    print("#" + str(test_case + 1) + " " +" ".join(map(str, answer[test_case])))