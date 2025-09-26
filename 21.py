class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        pos = {}
        n = len(nums1)

        for i in range(len(nums1)):
            pos[nums1[i]] = i

        arr = []
        for i in nums2:
            arr.append(pos[i])

        n = len(arr)
        ndash = 1
        while ndash < n:
            ndash *= 2

        st = [0]*(4*ndash)

        def query(index, ss, se, qs, qe):
            if ss > qe or se < qs:
                return 0

            if qs <= ss and qe >= se:
                return st[index]

            mid = (ss + se) // 2
            return query(2*index + 1, ss, mid, qs, qe) + \
                    query(2*index + 2, mid + 1, se, qs, qe)

        def update(index, arr_index, ss, se):
            if ss == se:
                st[index] += 1
                return    

            mid = (ss + se)//2
            if arr_index <= mid:
                update(2*index + 1, arr_index, ss, mid)
            else:
                update(2*index + 2, arr_index, mid + 1, se)

            st[index] = st[2*index + 1] + st[2*index + 2]

        count = 0

        st = [0]*(4*ndash) 
        left_smaller = [0]*n

        for i in range(n):
            left_smaller[i] = query(0, 0, ndash - 1, 0, arr[i] - 1)
            update(0, arr[i], 0, ndash - 1)

        st = [0]*(4*ndash) 
        right_greater = [0]*n

        for i in range(n-1, -1, -1):
            right_greater[i] = query(0, 0, ndash - 1, arr[i] + 1, ndash - 1)
            update(0, arr[i], 0, ndash - 1)    

        for i in range(n):
            count += left_smaller[i] * right_greater[i]
        return count    



