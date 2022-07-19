class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not self.flatten_rec(head): return None
        return head

    def flatten_rec(self, head):
        curr = head
        tail = head

        while curr:
            nxt = curr.next
            if curr.child:
                curr.next = curr.child
                curr.child.prev = curr
                tail = self.flatten_rec(curr.child)
                tail.next = nxt
                if nxt:
                    nxt.prev = tail
                curr.child = None
                curr = tail
            else:
                curr = nxt
            if curr:
                tail = curr
        return tail

    def flatten_iter(self, head):
        prev = Node()
        prev.next = head
        curr = head

        while curr:
            if curr.child:
                temp = curr.next
                curr.child.prev = curr
                curr.next = curr.child
                child = curr.child
                while child.next:
                    child = child.next
                child.next = temp
                if child.next:
                    child.next.prev = child
            curr.child = None
            curr = curr.next
        return prev.next

