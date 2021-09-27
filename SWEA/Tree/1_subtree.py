## 5174. subtree (09.27)
def inorder(node):
    global count
    if node == 0:
        return
    count += 1
    inorder(left[node])
    inorder(right[node])

T = int(input())
answer = []
for test_case in range(1, T + 1):
    e, n = map(int, input().split())
    input_list = list(map(int, input().split()))
    left = [0] * (e+2)
    right = [0] * (e+2)

    for i in range(0, len(input_list), 2):
        parent, child = input_list[i], input_list[i+1]
        if left[parent]: # 0이 아니고 첫번째 값에 있으면
            right[parent] = child
        else:
            left[parent] = child

    count = 0
    inorder(n)
    answer.append(count)


for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))