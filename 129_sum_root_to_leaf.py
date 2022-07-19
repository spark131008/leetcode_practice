from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node, num) -> int:
            if not node: return 0

            num = (num * 10) + node.val
            if not node.left and not node.right: return num

            left = helper(node.left, num)
            right = helper(node.right, num)
            return left + right
        return helper(root, 0)
