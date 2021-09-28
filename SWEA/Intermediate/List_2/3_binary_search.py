## 4839. 이진 탐색 (09.07)
T = int(input())
answer = []

def binary_search(target, start, end, count):
    if start > end:
        return 1e9
    mid = (start + end) // 2
    if mid > target:
        return binary_search(target, start, mid, count + 1)
    elif mid < target:
        return binary_search(target, mid, end, count + 1)
    else:
        return count + 1

for test_case in range(1, T + 1):
    p, pa, pb = map(int, input().split())
    result_a = binary_search(pa, 1, p, 0)
    result_b = binary_search(pb, 1, p, 0)
    if result_a > result_b:
        answer.append("B")
    elif result_a < result_b:
        answer.append("A")
    else:
        answer.append("0")

for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))