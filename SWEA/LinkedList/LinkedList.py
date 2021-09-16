## 링크드 리스트 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        current = self.head
        while current is not None:
            current = current.next
        current.next = Node(value)

    def print_all(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def get_node(self, index): # 인덱스 부분의 원소를 얻어옴
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value): # 원소 추가
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node

        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def delete_node(self, index): # 인덱스 부분의 원소 삭제
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index - 1)
        node.next = node.next.next

