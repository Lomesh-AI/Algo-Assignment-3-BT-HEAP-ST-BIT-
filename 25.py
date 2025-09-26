from typing import List, Tuple
import bisect

class SegmentTree:
    def __init__(self, n: int):
        self.seg: List[int] = [0] * (4 * n + 1)
        self.n = n

    def build(self, idx: int, low: int, high: int, sum_list: List[int]):
        if low == high:
            self.seg[idx] = sum_list[low]
            return

        mid = (low + high) // 2
        self.build(2 * idx + 1, low, mid, sum_list)
        self.build(2 * idx + 2, mid + 1, high, sum_list)

        self.seg[idx] = max(self.seg[2 * idx + 1], self.seg[2 * idx + 2])

    def query(self, idx: int, low: int, high: int, l: int, r: int) -> int:
        if l > high or low > r:
            return 0
        if low >= l and high <= r:
            return self.seg[idx]

        mid = (low + high) // 2
        left = self.query(2 * idx + 1, low, mid, l, r)
        right = self.query(2 * idx + 2, mid + 1, high, l, r)

        return max(left, right)

class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        
        v: List[Tuple[int, int]] = sorted(
            zip(nums1, nums2), 
            key=lambda p: p[0], 
            reverse=True
        )

        maxY = -1
        x: List[int] = []
        y: List[int] = []
        sum_list: List[int] = []

        for val_x, val_y in v:
            if val_y > maxY:
                maxY = val_y
                x.append(val_x)
                y.append(val_y)
                sum_list.append(val_x + val_y)

        if not sum_list:
            return [-1] * len(queries)
            
        sg = SegmentTree(len(sum_list))
        sg.build(0, 0, len(sum_list) - 1, sum_list)

        def bisect_right_custom(xi: int) -> int:
            low, high = 0, len(x) - 1
            ans = -1
            while low <= high:
                mid = low + (high - low) // 2
                if x[mid] >= xi:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans

        ans: List[int] = []
        for xi, yi in queries:
            
            curr = bisect_right_custom(xi)
            
            if curr == -1:
                ans.append(-1)
                continue

            nxt = bisect.bisect_left(y, yi)
            
            if nxt == len(y) or nxt > curr:
                ans.append(-1)
                continue

            max_sum = sg.query(0, 0, len(sum_list) - 1, nxt, curr)
            ans.append(max_sum if max_sum > 0 else -1)
            
        return ans