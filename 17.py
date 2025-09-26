from collections import defaultdict
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n = len(nums)

        sorted_arr = sorted(set(nums))
        m = len(sorted_arr)

        indexes = {val: index for index, val in enumerate(sorted_arr)}

        ndash = 1
        while ndash < m:
            ndash *= 2

        st = [0]*(4*ndash)

        def query(index, ss, se, qs, qe):
            if ss > qe or se < qs:
                return float('-inf')

            if qs <= ss and qe >= se:
                return st[index]

            mid = (ss + se)//2
            return max(query(2*index + 1, ss, mid, qs, qe), \
                        query(2*index + 2, mid + 1, se, qs, qe))

        def update(index, arr_index, ss, se, val):
            if ss == se:
                st[index] = val
                return

            mid = (ss + se)//2
            if arr_index <= mid:
                update(2*index + 1, arr_index, ss, mid, val)
            else:
                update(2*index + 2, arr_index, mid + 1, se, val)

            st[index] = max(st[2*index + 1], st[2*index + 2])    


        for i in range(n):

            index1 = bisect.bisect_left(sorted_arr, nums[i] - k)
            index2 = bisect.bisect_right(sorted_arr, nums[i] - 1) - 1

            if index1 <= index2:
                maxx = query(0, 0, ndash - 1, index1, index2) + 1 
                update(0, indexes[nums[i]], 0, ndash - 1, maxx)
            else:
                update(0, indexes[nums[i]], 0, ndash - 1, 1)

        return st[0]              








