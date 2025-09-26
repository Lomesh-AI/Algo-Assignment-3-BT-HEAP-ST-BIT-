class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxx = float('-inf')

        def helper(root):
            nonlocal maxx
            if not root:
                return 0

            left = helper(root.left)
            right = helper(root.right)
            maxx = max(maxx, left + right)
            return 1 + max(left, right)

        _ = helper(root)
        return maxx    
