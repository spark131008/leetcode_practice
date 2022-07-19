from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if (p.val if p else 0) != (q.val if q else 0): return False

        leftNode = self.isSameTree(p.left if p else None, q.left if q else None)
        rightNode = self.isSameTree(p.right if p else None, q.right if q else None)
        return leftNode and rightNode