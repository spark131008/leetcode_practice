class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if not self.head:
            return -1

        curr = self.head
        while index and curr:
            curr = curr.next
            index -= 1
        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        new = Node(val=val)
        new.next = self.head
        self.head = new

    def addAtTail(self, val: int) -> None:
        new = Node(val=val)
        if self.head:
            curr = self.head
            prev = None
            while curr:
                prev, curr = curr, curr.next
            prev.next = new
        else:
            self.head = new

    def addAtIndex(self, index: int, val: int) -> None:
        if not index:
            self.addAtHead(val)
            return None

        if self.head:
            curr = self.head
            prev = None
            while index and curr:
                prev, curr = curr, curr.next
                index -= 1
            if not index:
                temp = prev.next
                prev.next = Node(val=val, next=temp)

        else:
            if not index:
                self.addAtHead(val)

    def deleteAtIndex(self, index: int) -> None:
        if self.head:
            if not index:
                self.head = self.head.next
                return None

            curr = self.head
            prev = None
            while index and curr:
                prev, curr = curr, curr.next
                index -= 1
            if not index and curr:
                prev.next = curr.next