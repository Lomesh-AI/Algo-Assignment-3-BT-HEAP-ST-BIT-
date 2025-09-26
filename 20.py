class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        n = len(nums1)
        arr = []
        for i in range(n):
            arr.append(nums1[i] - nums2[i])

        sorted_arr = sorted(set(arr))
        m = len(sorted_arr)
        bit = [0]*(m + 1)

        def get_rank(x):
            l = 0
            r = m-1

            while l<=r:
                mid = (l + r)//2

                if sorted_arr[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1
            return l + 1

        def update(i, delta):
            while i<=m:
                bit[i] += delta
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        count = 0
        for i in range(n-1, -1, -1):
            rank1 = get_rank(arr[i] - diff)
            rank2 = get_rank(arr[i])
            count += query(m) - query(rank1-1)
            update(rank2, 1)

        return count    



