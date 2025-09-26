from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = [root]
        level = 0

        while q:
            size = len(q)
            dq = deque([])
            for _ in range(size): 
                node = q.pop(0)
                if level%2==0:
                    dq.append(node.val)
                else:
                    dq.appendleft(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)        
            level += 1
            res.append(list(dq))
        return res    