class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        n = len(rating)

        sorted_arr = sorted(set(rating))
        m = len(sorted_arr)

        left_bit = [0]*(m + 1)
        right_bit = [0]*(m + 1)

        def get_rank(x):
            l = 0
            r = m - 1

            while l<=r:
                mid = (l + r)//2
                if sorted_arr[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1
            return l + 1            

        def query(bit, i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        def update(bit, i, delta):
            while i <= m:
                bit[i] += delta
                i += i &-i

        right_smaller = [0]*n
        right_greater = [0]*n
        for i in range(n-1, -1, -1):
            rank = get_rank(rating[i])
            right_smaller[i] = query(right_bit, rank - 1)
            right_greater[i] = n - i - 1 - right_smaller[i]
            update(right_bit, rank, 1)

        left_smaller = [0]*n 
        left_greater = [0]*n
        for i in range(n):
            rank = get_rank(rating[i])
            left_smaller[i] = query(left_bit, rank - 1)
            left_greater[i] = i - left_smaller[i]
            update(left_bit, rank, 1)

        count = 0
        for i in range(n):
            count += left_smaller[i] * right_greater[i]
            count += left_greater[i] * right_smaller[i]
        return count        



