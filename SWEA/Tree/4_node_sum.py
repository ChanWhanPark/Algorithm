## 5178. 노드의 합 (09.27)
class Tree:
    def __init__(self, n):
        self.lst = [0] * (n+1)
        self.n = n

    def put(self, num1, num2):
        self.lst[num1] = num2

    def search_leaf(self, node):
        if node * 2 > n:
            self.sum += self.lst[node]
        else:
            self.search_leaf(node*2)
            if node*2 != n:
                self.search_leaf(node*2 + 1)

    def result(self, L):
        self.sum = 0
        self.search_leaf(L)
        return self.sum

T = int(input())
answer = []
for test_case in range(1, T + 1):
    n, m, l = map(int, input().split())
    tree = Tree(n)
    for _ in range(m):
        num1, num2 = map(int, input().split())
        tree.put(num1, num2)

    answer.append(tree.result(l))


for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))