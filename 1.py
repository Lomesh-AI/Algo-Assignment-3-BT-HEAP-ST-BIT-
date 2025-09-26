class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(root, target):
            if not root:
                
                return False 
            if not root.left and not root.right:
                if target == root.val:
                    return True
                return False     

            return dfs(root.left, target - root.val) or dfs(root.right, target - root.val) 

        return dfs(root, targetSum)
        