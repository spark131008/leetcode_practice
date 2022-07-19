from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root]) if root else None

        while q:
            subres = []
            for i in range(len(q)):
                num = q.popleft()
                subres.append(num.val)

                if num.left:
                    q.append(num.left)
                if num.right:
                    q.append(num.right)
            res.append(subres)
        return res

