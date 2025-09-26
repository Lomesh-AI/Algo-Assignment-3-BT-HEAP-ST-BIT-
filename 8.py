# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        count = 0
        def dfs(root):
            nonlocal count
            if not root:
                return 'O'

            left = dfs(root.left)
            right = dfs(root.right)

            if left == 'O' and right == 'O':
                return 'N'

            if left == 'N' or right == 'N':
                count += 1
                return 'C'

            if left == 'C' or right == 'C':
                return 'O'


        if dfs(root) == 'N':
            count += 1
        return count