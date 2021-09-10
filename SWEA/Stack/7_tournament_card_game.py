## 4880. 토너먼트 카드게임(09.10)
T = int(input())
answer = []

def winner(left, right):
    if student[left-1] == 1 and student[right-1] == 2:
        return right
    if student[left-1] == 2 and student[right-1] == 3:
        return right
    if student[left-1] == 3 and student[right-1] == 1:
        return right
    else:
        return left

def check(start, end):
    if start == end:
        return start
    else:
        mid = (start + end) // 2
        left_value = check(start, mid)
        right_value = check(mid+1, end)
        return winner(left_value, right_value)

for test_case in range(1, T + 1):
    n = int(input())
    student = list(map(int, input().split()))
    result = check(1, n)
    answer.append(result)


for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))