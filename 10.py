class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        front = []
        back = []
        
        cost = 0
        i = 0
        j = n - 1

        while k:
            while len(front) < candidates and i <= j:
                heapq.heappush(front, costs[i])
                i += 1

            while len(back) < candidates and i <= j:
                heapq.heappush(back, costs[j])
                j -= 1

            if front and back:
                if front[0] > back[0]:
                    cost += heapq.heappop(back)
                else:
                    cost += heapq.heappop(front)

            elif front and k:
                cost += heapq.heappop(front)

            elif back and k:
                cost += heapq.heappop(back)
                
            k -= 1    

        return cost        

