from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot: return True
        if not root: return False

        def isSametree(t1, t2) -> bool:
            if not t1 and not t2: return True
            if not t1 or not t2: return False
            leftNode = isSametree(t1.left, t2.left)
            rightNode = isSametree(t1.right, t2.right)
            return leftNode and rightNode and t1.val == t2.val

        if isSametree(root, subRoot): return True
        leftNode = self.isSubtree(root.left, subRoot)
        rightNode = self.isSubTree(root.right, subRoot)
        return leftNode or rightNode