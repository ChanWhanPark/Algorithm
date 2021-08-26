## 재귀함수를 이용한 DFS 구현(08.26)
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
visited = []
visited2 = []

def dfs_recursive(graph, cur_node, visited_array):
    visited_array.append(cur_node)
    for node in graph:
        if node not in visited_array:
            dfs_recursive(graph, node, visited_array)
    return visited_array

dfs_recursive(graph, 1, visited)
print(visited)

dfs_recursive(graph2, 1, visited2)
print(visited2)