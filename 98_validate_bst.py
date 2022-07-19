from typing import Optional
import math
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node: TreeNode, left: int, right: int) -> bool:
            if not node: return True
            if not(node.val > left and node.val < right): return False

            leftNode = helper(node.left, left, node.val)
            rightNode = helper(node.right, node.val, right)
            return leftNode and rightNode
        return helper(root, -sys.maxsize, sys.maxsize)