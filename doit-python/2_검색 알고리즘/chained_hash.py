#2-5. 체인법 헤쉬 함수

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    # 해시를 구성하는 노드
    def __init__(self, key:Any, value:Any, next:Node) -> None:
        self.key = key
        self.value = value
        self.next = next

class ChainedHash:
    # 체인법
    def __init__(self, capacity: int)-> None:
        self.capacity = capacity # 해시 테이블의 크기
        self.table = [None] * self.capacity # 해시 테이블 선언

    def hash_value(self, key: Any)-> int:
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any:
        hash = self.hash_value(key) # 검색하는 키의 해시값
        p = self.table[hash] #노드

        while p is not None:
            if p.key == key:
                return p.value # 검색 성공
            p = p.next

        return None # 검색 실패

    def add(self, key: Any, value:Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False # 추가 실패
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp # 노드를 추가
        return True

    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False

    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' ->{p.key}({p.value})', end='')
                p = p.next
            print()
