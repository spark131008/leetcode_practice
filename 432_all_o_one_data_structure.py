
## Raw Approach
class AllOne:

    def __init__(self):
        self.hashMap = {}

    def inc(self, key: str) -> None:
        if key in self.hashMap:
            self.hashMap[key] = self.hashMap[key] + 1
        else:
            self.hashMap[key] = 1

    def dec(self, key: str) -> None:
        if key in self.hashMap:
            if self.hashMap[key]:
                self.hashMap[key] = self.hashMap[key] - 1
            if not self.hashMap[key]:
                del self.hashMap[key]

    def getMaxKey(self) -> str:
        if not self.hashMap:
            return ""

        maxKeyMap = {}
        for key, count in self.hashMap.items():
            maxKeyMap[count] = key

        maxKeyCount = max(maxKeyMap)
        return maxKeyMap[maxKeyCount]

    def getMinKey(self) -> str:
        if not self.hashMap:
            return ""
        minKeyMap = {}
        for key, count in self.hashMap.items():
            minKeyMap[count] = key

        minKeyCount = min(minKeyMap)
        return minKeyMap[minKeyCount]

## Optimized Approach

import sys

class Node:
    def __init__(self, key, val, prev, next):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class AllOne:

    def __init__(self):
        self.hashMap = {}
        # left is a dummy node with a smallest val, right is a dummy node with a largest val
        self.left = Node("", -sys.maxsize)
        self.right = Node("", sys.maxsize)
        self.left.next, self.right.prev = self.right, self.left

    # insert a new node only next to the dummy left pointer
    def insert(self, node: Node):
        prv, nxt = self.left, self.left.next
        node.prev, node.next = prv, nxt
        prv.next = nxt.prev = node

    def remove(self, node: Node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def switch(self, n1, n2):
        farLeft, farRight = n1.prev, n2.next
        farLeft.next = n2
        farRight.prev = n1
        n2.prev = farLeft
        n1.next = farRight
        n2.next, n1.prev = n1, n2

    def inc(self, key: str) -> None:
        if key in self.hashMap:
            self.hashMap[key].val = self.hashMap[key].val + 1
            # switch newly added node(far left) with the next node on the right.
            # do this until its val is no longer larger than its neighbor node's val
            while self.hashMap[key].val > self.hashMap[key].next.val:
                self.switch(self.hashMap[key], self.hashMap[key].next)
        else:
            self.hashMap[key] = Node(key, 1)
            self.insert(self.hashMap[key])

    def dec(self, key: str) -> None:
        if key in self.hashMap:
            self.hashMap[key].val = self.hashMap[key].val - 1

            # when the node.val == 0, remove it from the doubely linked list and from the hashMap
            if not self.hashMap[key].val:
                self.remove(self.hashMap[key])
                del self.hashMap[key]

            else:
                # switch the existing node with the next node on the left.
                # do this until its val is no longer smaller than its neighbor node's val
                while self.hashMap[key].val < self.hashMap[key].prev.val:
                    self.switch(self.hashMap[key].prev, self.hashMap[key])

    def getMaxKey(self) -> str:
        if not self.hashMap:
            return ""
        return self.right.prev.key

    def getMinKey(self) -> str:
        if not self.hashMap:
            return ""
        return self.left.next.key