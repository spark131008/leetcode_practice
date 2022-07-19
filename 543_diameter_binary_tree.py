from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = [0]

        def helper(root) -> int:
            if not root: return -1

            left = helper(root.left)
            right = helper(root.right)
            maxDiameter[0] = max(maxDiameter[0], (2+left+right))
            return max(left, right) + 1
        helper(root)
        return maxDiameter[0]