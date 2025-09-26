from collections import defaultdict
import math
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        d = defaultdict(int)
        max_stone = float('-inf')
        for i in piles:
            d[i] += 1
            max_stone = max(max_stone, i)

        for i in range(max_stone, 0, -1):
            if i in d:
                while k and d[i]:
                    remaining = i - i//2
                    d[i] -= 1
                    d[remaining] += 1
                    k -= 1
            if not k:
                break
        
        res = 0
        for key, val in d.items():
            res += key * val

        return res    









