## 5176. 이진 탐색 (09.27)
def binary_search(node):
    global count
    if node <= n:
        binary_search(node*2)
        tree[node] = count
        count += 1
        binary_search(node*2 + 1)

T = int(input())
answer = []
for test_case in range(1, T + 1):
    n = int(input())
    tree = [0 for i in range(n+1)]
    count = 1
    binary_search(1)
    answer.append([tree[1], tree[n//2]])
    print(tree)


for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case][0]) + " " + str(answer[test_case][1]))