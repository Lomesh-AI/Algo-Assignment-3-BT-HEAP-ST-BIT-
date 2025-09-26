from typing import List

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        N = n + 2

       
        def update(bit, i, delta):
            while i < N:
                bit[i] += delta
                i += i & -i

        def query(bit, i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        left = [0] * N
        ans = 0

        for i in range(n):
            right = [0] * N
            for j in range(n-1, i, -1):
                if nums[i] > nums[j]:
                    l = query(left, nums[j] - 1)  
                    r = query(right, n) - query(right, nums[i])  
                    ans += l * r
                update(right, nums[j], 1)
            update(left, nums[i], 1)

        return ans
