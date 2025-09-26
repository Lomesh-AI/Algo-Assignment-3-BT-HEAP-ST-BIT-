class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        maxx = float('-inf')

        if not root:
            return 0

        def dfs(root):
            nonlocal maxx
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            left_path = 0
            right_path = 0

            if root.left and root.val == root.left.val:
                left_path = left + 1

            if root.right and root.right.val == root.val:
                right_path = right + 1

            maxx = max(maxx, left_path + right_path)

            return max(left_path, right_path)

        dfs(root)    
        return maxx