class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        n = len(mat)

        def count_small(mat, val):
            count = 0
            col = 0
            row = n-1

            while col < n and row > -1:
                if mat[row][col] <= val:
                    count += row + 1
                    col += 1
                else:
                    row -= 1  

            return count                   

        l = mat[0][0]
        r = mat[n-1][n-1]
        ans = -1
        while l <= r:
            mid = l + (r-l)//2
            rank = count_small(mat, mid)

            if rank >= k:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans            
