class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def getHeight(root):
            if not root:
                return 0

            leftHeight = getHeight(root.left)
            rightHeight = getHeight(root.right)  

            if leftHeight == -1 or rightHeight == -1:
                return -1
            if abs(leftHeight - rightHeight) > 1:
                return -1

            return 1 + max(leftHeight, rightHeight)

        height = getHeight(root)
        return True if height != -1 else False 