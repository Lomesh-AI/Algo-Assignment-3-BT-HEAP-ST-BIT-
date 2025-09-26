class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for i in nums:
            i.sort()

        score = 0
        cols = len(nums[0])
        rows = len(nums)

        for col in range(cols):
            maxx = float('-inf')
            for row in range(rows):
                maxx = max(maxx, nums[row][col])
            score += maxx

        return score        

