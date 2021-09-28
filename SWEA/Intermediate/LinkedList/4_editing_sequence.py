## 5122. 수열 편집
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        new_node = Node('head')
        self.head = new_node
        self.tail = new_node

        self.before = None
        self.current = None
        self.num_of_data = 0

    def append(self, data):
        new_node = Node(data)
        self.tail.link = new_node
        self.tail = new_node


    def move_to(self, D):
        self.current = self.head.link
        self.before = self.head
        for _ in range(D):
            if self.current == None:
                return False
            self.before = self.current
            self.current = self.current.link
        return True

    def insert(self, index, data):
        new_node = Node(data)
        self.move_to(index)
        self.before.link = new_node
        new_node.link = self.current

    def delete(self, index):
        self.move_to(index)
        self.before.link = self.current.link

    def change(self, index, data):
        self.move_to(index)
        self.current.data = data

    def get_result(self, index):
        if self.move_to(index):
            return self.current.data
        else:
            return -1



T = int(input())
answer = []
for test_case in range(1, T + 1):
    n, m, l = map(int, input().split())
    lst = list(map(int, input().split()))
    sequence = LinkedList()
    for i in lst:
        sequence.append(i)

    for _ in range(m):
        op = list(input().split())
        if op[0] == 'I':
            sequence.insert(int(op[1]), int(op[2]))
        elif op[0] == 'D':
            sequence.delete(int(op[1]))
        elif op[0] == 'C':
            sequence.change(int(op[1]), int(op[2]))

    answer.append(sequence.get_result(l))


for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))