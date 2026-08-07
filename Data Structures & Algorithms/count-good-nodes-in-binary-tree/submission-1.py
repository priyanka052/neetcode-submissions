# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if node is None:
                return 0
            count = 0
            if node.val >= max_so_far:
                count = 1
                max_so_far = max(max_so_far, node.val)
            left = dfs(node.left, max_so_far)
            right = dfs(node.right, max_so_far)
            return count + left + right
        return dfs(root, root.val)