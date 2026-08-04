# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.daimeter = 0
        def height(node):
            if node is None:
                return 0
            left = height(node.left)
            right = height(node.right)
            self.daimeter =  max(self.daimeter, right+left)
            return 1 + max(left, right)
        height(root)
        return self.daimeter