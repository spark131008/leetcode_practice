class Node:
    def __init__(self, key=0, val=0, counter=1, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        self.counter = counter


import sys


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.left = Node(counter=-sys.maxsize)
        self.right = Node(counter=sys.maxsize)
        self.left.next, self.right.prev = self.right, self.left

    def switch(self, node1, node2):
        farLeft, farRight = node1.prev, node2.next
        farLeft.next = node2
        node2.prev = farLeft
        farRight.prev = node1
        node1.next = farRight
        node2.next, node1.prev = node1, node2

    def add(self, node):
        nxt = self.left.next
        self.left.next = node
        node.prev = self.left
        node.next = nxt
        nxt.prev = node

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.hashMap[key].counter += 1
            while self.hashMap[key].counter >= self.hashMap[key].next.counter:
                self.switch(self.hashMap[key], self.hashMap[key].next)
            return self.hashMap[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
            del self.hashMap[key]
        if self.capacity:
            if self.capacity == len(self.hashMap):
                lru = self.left.next
                self.remove(self.hashMap[lru.key])
                del self.hashMap[lru.key]

            self.hashMap[key] = Node(key=key, val=value)
            self.add(self.hashMap[key])
            while self.hashMap[key].counter >= self.hashMap[key].next.counter:
                self.switch(self.hashMap[key], self.hashMap[key].next)