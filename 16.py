import bisect
class Solution:
   def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
      
        n = len(nums)
        prefix = [0]*(n+1)
        prefix[0] = 0


        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        # print(prefix)   


        sorted_arr = sorted(set(prefix))
        m = len(sorted_arr)
        
        ndash = 1
        while ndash < m:
            ndash *= 2
        
        st = [0]*(2*ndash)

        def query(start, end, ss, se, index):
            if end < ss or start > se:
                return 0

            if start <= ss and end >= se:
                return st[index]

            mid = (ss+se)//2
            return query(start, end, ss, mid, 2*index + 1) + query(start, end, mid + 1, se, 2*index + 2) 

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
        for j in range(n+1):
            index1 = bisect.bisect_left(sorted_arr, prefix[j] - upper)
            index2 = bisect.bisect_right(sorted_arr, prefix[j] - lower) - 1
            count += query(index1, index2, 0, ndash-1, 0)
            index = bisect.bisect_left(sorted_arr, prefix[j])
            update(0, index, 0, ndash - 1)

        return count    



