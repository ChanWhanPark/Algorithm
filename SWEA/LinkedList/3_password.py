## 5120. 암호 (09.16)
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
        self.tail.link = self.head.link # 첫 요소와 끝을 연결
        self.num_of_data += 1

    def first(self): # 첫 요소 가져오기
        self.current = self.head.link
        self.before = self.tail
        return self.current.data

    def next(self):
        self.before = self.current
        self.current = self.current.link
        return self.current.data

    def insert(self, data):
        new_node = Node(data)
        self.before.link = new_node
        new_node.link = self.current
        self.current = new_node
        self.num_of_data += 1

    def make_password(self, num):
        for _ in range(num):
            self.next()
        num = self.before.data + self.current.data
        self.insert(num)

    def result(self):
        final_lst = [self.first()]
        for _ in range(self.num_of_data - 1):
            final_lst.append(self.next())

        return ' '.join(map(str, final_lst[-1:-11:-1]))


T = int(input())
answer = []
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    lst = list(map(int, input().split()))
    sequence = LinkedList()
    for i in lst:
        sequence.append(i)
    sequence.first()
    for _ in range(k):
        sequence.make_password(m)

    answer.append(sequence.result())




for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))