from typing import Optional, List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right

    def recursiveSol(self, root, k) -> int:
        res = []

        def helper(node):
            if not node: return None
            helper(node.left)
            res.append(node.val)
            helper(node.right)

        helper(root)
        return res[k-1]

    def recursiveSol2(self, root, k) -> int:
        # inorder BST traversal
        def helper(node) -> List:
            return helper(node.left) + [node.val] + helper(node.right) if node else []

        return helper(root)[k-1]

    def recursiveSol3(self, root, k) -> int:
        # preorder BST traversal
        def helper(node) -> List:
            return [node.val] + helper(node.left) + helper(node.right) if node else []

        return helper(root)[k-1]