## 타겟 넘버 (10.07)
def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def DFS(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            DFS(idx+1, result + numbers[idx])
            DFS(idx+1, result - numbers[idx])

    DFS(0, 0)
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3

print(solution(numbers, target))