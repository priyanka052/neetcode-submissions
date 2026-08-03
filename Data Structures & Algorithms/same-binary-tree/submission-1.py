# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):

        # Base Case 1
        if not p and not q:
            return True

        # Base Case 2
        if not p or not q:
            return False

        # Compare values
        if p.val != q.val:
            return False

        # Recurse on left
        left = self.isSameTree(p.left, q.left)

        # Recurse on right
        right = self.isSameTree(p.right, q.right)

        # Return
        return left and right
            