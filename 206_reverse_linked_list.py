class ListNode:
    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverselist_iter(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    '''
    ex) None   ->   1   ->   2   ->   3   ->   None
    1)  (prev)   (curr)  (curr.next)
    1.1) Make (curr.next) point to (prev), and store curr.next in nextPointer in advance
    
    2) (curr.next) <- (curr)
    2.1) Now the the linked list is reversed. Then, move (prev) and (curr) pointers to the next node
    2.2) (prev) = (curr)
    2.3) (curr) = (next)
    
    3) return (prev) because this while-loop will continue until (curr) hits None.
    '''



    def reverselist_recur(self, head: ListNode) -> ListNode:
        if not head: return None

        newHead = head
        if head.next:
            newHead = self.reverselist_recur(head.next)
            head.next.next = head
        head.next = None
        return newHead