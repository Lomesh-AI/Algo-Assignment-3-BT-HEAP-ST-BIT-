class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapp = {}
        n = len(preorder)
        m = len(inorder)
        for i in range(n):
            for j in range(m):
                if preorder[i] == inorder[j]:
                    mapp[preorder[i]] = j
                    break

        def helper(pres, preend, ins, inend):
            nonlocal mapp
            if pres > preend or ins > inend:
                return None

            data = preorder[pres]
            node = TreeNode(data)
            index = mapp[data]

            no_of_elements_left = index - ins
            node.left = helper(pres+1, pres + no_of_elements_left, ins, index-1)
            node.right = helper(pres + no_of_elements_left + 1, preend, index + 1, inend)

            return node

        return helper(0, n-1, 0, m-1)