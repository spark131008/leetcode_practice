from typing import Optional, List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

    def buildTree1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorderIndexMap = {}
        for index, val in enumerate(inorder):
            inorderIndexMap[val] = index

        preorderIndex = 0

        def helper(leftIndex, rightIndex):
            nonlocal preorderIndex

            if leftIndex > rightIndex or rightIndex < leftIndex: return None

            rootVal = preorder[preorderIndex]
            preorderIndex += 1
            root = TreeNode(rootVal)
            midIndex = inorderIndexMap[rootVal]

            root.left = helper(leftIndex, midIndex-1)
            root.right = helper(midIndex+1, rightIndex)
            return root
        return helper(0, len(inorder)-1)
