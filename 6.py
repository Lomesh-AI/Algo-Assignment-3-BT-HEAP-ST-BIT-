class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(root, p, q):
            if not root or root == p or root == q:
                return root

            left = helper(root.left, p, q)
            right = helper(root.right, p, q)

            if not left and not right:
                return None
            elif not left:
                return right
            elif not right:
                return left
            else:
                return root # both are not null

        return helper(root, p, q)                    
