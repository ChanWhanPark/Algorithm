def solution(n, queries):
    answer = []
    queue = [[] for _ in range(n)]
    pointer = 0
    next_pop_value = -100001
    for q in queries:
        print(queue)
        if q[0] != -1:
            queue[q[0]].append(q[1])
            if next_pop_value == -100001:
                next_pop_value = queue[pointer].pop(0)
        else:
            if len(queue[pointer]) == 0:
                pointer += 1
            else:
                answer.append(next_pop_value)
                next_pop_value = queue[pointer].pop(0)
                pointer += 1
                if pointer == n:
                    pointer = 0

    print(next_pop_value)
    print(queue)
    return answer

print(solution(4, [[0, 1], [0, 2], [0, 3], [3, 4], [1, 5], [3, 6], [2, 7], [3, 8], [1, 9], [-1, -1],
                   [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]))