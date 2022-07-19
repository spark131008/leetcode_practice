from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth_DFS(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        leftNode = self.maxDepth(root.left)
        rightNode = self.maxDepth(root.right)
        return max(leftNode, rightNode) + 1

    def maxDepth_BFS(self, root) -> int:
        q = deque([root]) if root else None
        level = 0

        while q:
            for i in range(len(q)):
                node = q.pop()
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
            level += 1
        return level
