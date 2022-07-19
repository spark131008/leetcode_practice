# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, maxVal) -> int:
            if not node: return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += helper(node.left, maxVal)
            res += helper(node.right, maxVal)
            return res
        return helper(root, root.val)