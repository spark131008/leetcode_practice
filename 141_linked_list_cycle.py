from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle_1(self, head: Optional[ListNode]) -> bool:
        hashMap = {}

        while head:
            if head in hashMap:
                return True
            hashMap[head] = head.val
            head = head.next
        return False

    def hasCycl_2(self, head: Optional[ListNode]) -> bool:
        s, f = head, head

        while f:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False