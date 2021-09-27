## 5177. 이진 힙 (09.27)
T = int(input())
answer = []

class Tree:
    def __init__(self):
        self.lst = [0]

    def sort(self, num):
        if num >= 2:
            if self.lst[num] < self.lst[num // 2]:
                self.lst[num], self.lst[num // 2] = self.lst[num // 2], self.lst[num]
                self.sort(num // 2)

    def append(self, data):
        num = len(self.lst)
        self.lst.append(data)
        self.sort(num)

    def tree_sum(self, node):
        if node <= 1:
            return self.lst[node]
        else:
            return self.lst[node] + self.tree_sum(node//2)
    def result(self):
        last = len(self.lst) - 1
        self.sum = 0
        if last >= 2:
            return self.tree_sum(last//2)
        else:
            return 0

for test_case in range(1, T + 1):
    n = int(input())
    tree = Tree()
    input_list = list(map(int, input().split()))
    for i in input_list:
        tree.append(i)

    answer.append(tree.result())

for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))