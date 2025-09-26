class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        def query(index, ss, se, val):
            if not st[index][1] or st[index][0] < val:
                return -1

            if ss == se:
                return ss

            mid = (ss + se)//2
            left = query(2*index + 1, ss, mid, val)
            if left != -1:
                return left
            return query(2*index + 2, mid + 1, se, val)

        def update(index, ss, se, arr_index):
            if ss == se:
                st[index][1] = False
                return     

            mid = (ss + se)//2
            if arr_index <= mid:
                update(2*index + 1, ss, mid, arr_index)
            else:
                update(2*index + 2, mid + 1, se, arr_index)

            left = st[2*index + 1][0] if st[2*index + 1][1] else 0
            right =  st[2*index + 2][0] if st[2*index + 2][1] else 0
            st[index][0] = max(left, right)
            st[index][1] = st[2*index + 1][1] or st[2*index + 2][1]


        n = len(baskets)
        ndash = 1
        while ndash < n:
            ndash *= 2

        st = [[0, False] for _ in range(4*ndash)]

        for i in range(n):
            st[ndash - 1 + i] = [baskets[i], True]

        i = ndash - 2
        while i >= 0:
            st[i][0] = max(st[2*i + 1][0], st[2*i + 2][0])
            st[i][1] = st[2*i + 1][1] or st[2*i + 2][1]
            i -= 1

        count = 0

        for i in range(n):
            arr_index = query(0, 0, ndash - 1, fruits[i])    
            if arr_index == -1:
                count += 1
            else:
                update(0, 0, ndash - 1, arr_index)  
        return count          
