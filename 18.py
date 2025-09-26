class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        
        n = len(heights)

        ndash = 1
        while ndash < n:
            ndash *= 2

        st = [-1]*(4*ndash) 
        for i in range(n):
            st[ndash - 1 + i] = i

        i = ndash - 2
        while i >= 0:
            if st[2*i + 1] == -1:
                st[i] = st[2*i + 2]

            elif st[2*i + 2]  == -1:
                st[i] = st[2*i + 1]  

            elif heights[st[2*i + 1]] < heights[st[2*i + 2]]:
                st[i] = st[2*i + 2]

            else:
                st[i] = st[2*i + 1]
            i -= 1    

        def query_min_index_greater_height(st, a, qs, qe, ss, se, index):
            if qs > se or qe < ss:
                return -1

            if st[index] == -1 or heights[st[index]] <= heights[a]:
                return -1    

            if ss == se:
                return st[index]
                
            else:
                mid = (ss + se)//2
                left_index = query_min_index_greater_height(st, a, qs, qe, ss, mid, 2*index + 1)
                if left_index != -1:
                    return left_index
                return query_min_index_greater_height(st, a, qs, qe, mid + 1, se, 2*index + 2)

        res = []
        for query in queries:
            a = query[0]
            b = query[1]

            if a > b:
                a, b = b, a

            if a == b:
                res.append(a)

            elif heights[a] < heights[b]:
                res.append(b) 

            else:
                res.append(query_min_index_greater_height(st, a, b+1, \
                                                            n-1, 0, ndash - 1, 0))
        return res                        







    

