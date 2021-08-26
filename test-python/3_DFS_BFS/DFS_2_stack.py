## 스택을 이용한 DFS 구현(08.26)
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
} # 인접 리스트

graph2 = {
    1: [2, 3, 8],
    2: [1, 7],
    3: [1, 4, 5],
    4: [3, 5],
    5: [3, 4],
    6: [7],
    7: [2, 6, 8],
    8: [1, 7]
}


def dfs_stack(graph, node):
    stack = [node]
    visited = []

    while stack:
        current_node = stack.pop()
        visited.append(current_node)
        for n in graph[current_node]:
            if n not in visited:
                stack.append(n)

    return visited

print(dfs_stack(graph, 1))
print(dfs_stack(graph2, 1))

# 스택에 가장 마지막에 위치한 원소를 차출하므로 큰 수부터 꺼내는 결과