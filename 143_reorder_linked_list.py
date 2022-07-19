from typing import Optional

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def reorderList(self, head: Optional[ListNode]) -> None:
        slowPntr, fastPntr = head, head.next
        while fastPntr and fastPntr.next:
            slowPntr = slowPntr.next
            fastPntr = fastPntr.next.next

        tempSecondHead = slowPntr.next
        prev = slowPntr.next = None
        while tempSecondHead:
            next = tempSecondHead.next
            tempSecondHead.next = prev
            prev = tempSecondHead
            tempSecondHead = next

        firsthead, secondhead = head, prev
        while secondhead:
            temp1, temp2 = firsthead.next, secondhead.next
            firsthead.next = secondhead
            secondhead.next = temp1
            firsthead, secondhead = temp1, temp2