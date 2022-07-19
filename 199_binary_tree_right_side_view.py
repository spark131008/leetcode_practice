from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root]) if root else None
        res = []

        while q:
            rightSide = None
            qLength = len(q)
            for i in range(qLength):
                num = q.popleft()
                rightSide = num

                if num.left:
                    q.append(num.left)
                if num.right:
                    q.append(num.right)
            res.append(rightSide.val)
        return res